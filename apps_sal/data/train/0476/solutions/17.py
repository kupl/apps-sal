class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        N = len(position)
        cars = sorted((s,p) for s,p in zip(speed, position))
        seen = set()
        res = 0
        # print(cars)
        for i in range(N):
            if i in seen: continue
            seen.add(i)
            res += 1
            
            for j in range(i+1, N):
                if j in seen or cars[j][0]==cars[i][0]: continue
                t = (cars[i][1]-cars[j][1])/(cars[j][0]-cars[i][0])
                if t<0 or t*cars[i][0]+cars[i][1]>target: continue
                seen.add(j)
                
        return res

