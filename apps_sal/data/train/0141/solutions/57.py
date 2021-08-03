class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        ret = 0
        people.sort(reverse=True)
        start = len(people) - 1
        for i in range(len(people)):
            if start >= i:
                ret += 1
            temp_lim = limit - people[i]
            for j in range(start, i, -1):
                if people[j] <= temp_lim:
                    start = j - 1
                    break
                elif people[j] > temp_lim:
                    start = j
                    break

            print(temp_lim)
        return ret
