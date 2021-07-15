class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        light = [i-1 for i in light]
        bulbs = [0 for _ in range(len(light))]
        on,blue = set(),set()
        res = 0
        #print(bulbs)
        #print(light)
        n = len(light)
        total = 0
        for moment in light:
            #print(bulbs,moment)
            if moment == 0:
                bulbs[0] = 2
                blue.add(0)
            elif bulbs[moment-1] == 2:
                bulbs[moment] = 2
                blue.add(moment)
            else:
                bulbs[moment] = 1
                on.add(moment)
            if bulbs[moment] == 2:
                #print('turning things blue',bulbs[moment+1] if moment+1 < n else -1)
                i = moment+1
                while i < n and bulbs[i] == 1:
                    bulbs[i] = 2
                    blue.add(on.remove(i))
                    i += 1
            res += 1 if blue and not on else 0
        return res
