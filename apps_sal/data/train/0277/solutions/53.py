def fillMissingSet(highest_bulb, bulbs_missing, bulbs_lit, difference):
    for i in range(highest_bulb-difference,highest_bulb):
        if i not in bulbs_lit:
            bulbs_missing.add(i)

class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        highest_bulb = 1
        difference = 0
        bulbs_lit = set()
        bulbs_missing = set()
        instances=0
        fillMissingSet(light[0], bulbs_missing, bulbs_lit, difference)
        for i in range(len(light)):
            difference = 0
            if highest_bulb < light[i]:
                difference = light[i]-highest_bulb
                highest_bulb = light[i]
            bulbs_lit.add(light[i])
            if light[i] in bulbs_missing:
                bulbs_missing.remove(light[i])
            fillMissingSet(highest_bulb, bulbs_missing, bulbs_lit, difference)
            if len(bulbs_missing) == 0:
                instances +=1
            #print(highest_bulb, bulbs_missing, bulbs_lit, instances, difference)
        return instances
    


