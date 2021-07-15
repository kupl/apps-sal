class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        less_than_half = dict()
        more_than_half = dict()
        half = 0
        total_boats = 0
        for person in people:
            diff = limit - person
            if diff == 0:
                total_boats += 1
                continue
            if person < limit/2:
                if diff in more_than_half:
                    total_boats += 1
                    if more_than_half[diff] == 1:
                        del more_than_half[diff]
                    else:
                        more_than_half[diff] -= 1
                else:
                    if person in less_than_half:
                        less_than_half[person] += 1
                    else:
                        less_than_half[person] = 1
            elif person > limit/2:
                if diff in less_than_half:
                    total_boats += 1
                    if less_than_half[diff] == 1:
                        del less_than_half[diff]
                    else:
                        less_than_half[diff] -= 1
                else:
                    if person in more_than_half:
                        more_than_half[person] += 1
                    else:
                        more_than_half[person] = 1
            else:
                if half == 1:
                    total_boats += 1
                    half = 0
                else:
                    half = 1
        
        less_keys = sorted(less_than_half.keys())
        more_keys = sorted(list(more_than_half.keys()), reverse=True)
        
        while len(less_keys) and len(more_keys):
            if less_keys[0] + more_keys[0] <= limit:
                if less_than_half[less_keys[0]] < more_than_half[more_keys[0]]:
                    total_boats += less_than_half[less_keys[0]]
                    more_than_half[more_keys[0]] -= less_than_half[less_keys[0]]
                    less_keys.pop(0)
                elif less_than_half[less_keys[0]] > more_than_half[more_keys[0]]:
                    total_boats += more_than_half[more_keys[0]]
                    less_than_half[less_keys[0]] -= more_than_half[more_keys[0]]
                    more_keys.pop(0)
                else:
                    total_boats += less_than_half[less_keys[0]]
                    less_keys.pop(0)
                    more_keys.pop(0)
            else:
                total_boats += more_than_half[more_keys[0]]
                more_keys.pop(0)
                    
        less_total = 0
        for k in less_keys:
            less_total += less_than_half[k]
        
        more_total = 0
        for k in more_keys:
            more_total += more_than_half[k]
        
        # we can pair up each of the less than half weights
        total_boats += (less_total+half + 1) // 2 + more_total
        
        return total_boats


