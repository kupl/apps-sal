class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        len_lis = len(light)
        lis = [[] for x in range(len_lis+2)]
        tot = 0
        for i in range(len_lis):
            if(light[i] > 1 and lis[light[i]-1] and light[i] < len_lis and lis[light[i]+1]):
                end = lis[light[i]+1][1]
                start = lis[light[i]-1][0]
            elif(light[i] > 1 and lis[light[i]-1]):
                start = lis[light[i]-1][0]
                end = light[i]
            elif(light[i] < len_lis and lis[light[i]+1]):
                start = light[i]
                end = lis[light[i]+1][1]
            else:
                start = light[i]
                end = light[i]
            if(end-start == i and start == 1):
                tot += 1
            lis[end] = [start, end]
            lis[start] = [start, end]
            #print(lis)
        return tot
