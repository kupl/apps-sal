class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        max_time, time_map = 0, {}
        
        for curr in range(len(manager)):
            
            # memoization: backtracking to head or till the one we've
            # already seen before
            curr_em, curr_time = [], []
            while curr not in time_map and curr != -1:
                
                curr_em.append(curr)
                curr_time.append(informTime[curr])
                curr = manager[curr]
            
            # reconstruct the accumulated pathsum, save it in the map
            if curr_time:
                rest_time = time_map[curr] if curr != -1 else 0
                curr_time[-1] += rest_time
                time_map[curr_em[-1]] = curr_time[-1]
                for j in range(len(curr_time)-2, -1, -1):
                    curr_time[j] = curr_time[j+1] + curr_time[j]
                    time_map[curr_em[j]] = curr_time[j]
                    
                # compare every current longest pathsum with the currmax
                max_time = max(max_time, curr_time[0])
        return max_time
