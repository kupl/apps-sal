class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        stations = [[0,startFuel]] + sorted(stations)
        n = len(stations)        
        reach = [-float('inf')]*n
        reach[0] = startFuel
        st = [startFuel]*n
        flag = True
        cnt = 0
        if target <= startFuel:
            return 0
        while flag:
            flag = False
            cnt += 1
            for i in range(1,len(reach))[::-1]:
                p, g = stations[i]
                st.pop()
                if p <= st[-1] and st[-1] + g > reach[i]:
                    reach[i] = st[-1] + g
                    flag = True
                    if reach[i] >= target:
                        return cnt
            for i in range(1,len(reach)):
                st.append(max(st[-1],reach[i]))
            
        return -1
