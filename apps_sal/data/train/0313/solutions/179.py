class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        len_bloom = len(bloomDay)
        lis = [[bloomDay[i], i] for i in range(len_bloom)]
        lis.sort()
        lis2 = [[] for x in range(len_bloom)]
        tot = 0
        for i in lis:
            val, index = i
            if(index > 0 and lis2[index - 1] and index < len_bloom - 1 and lis2[index + 1]):
                start = lis2[index - 1][0]
                end = lis2[index + 1][1]
                tot -= (lis2[index - 1][3] + lis2[index + 1][3])
                tot_len = lis2[index - 1][2] + 1 + lis2[index + 1][2]
                tot += tot_len // k
                to_be_inserted = [start, end, tot_len, tot_len // k]
                lis2[start] = to_be_inserted
                lis2[end] = to_be_inserted
            elif(index > 0 and lis2[index - 1]):
                start = lis2[index - 1][0]
                end = index
                tot -= lis2[index - 1][3]
                tot_len = lis2[index - 1][2] + 1
                tot += tot_len // k
                lis2[start] = [start, end, tot_len, tot_len // k]
                lis2[end] = lis2[start]
            elif(index < len_bloom - 1 and lis2[index + 1]):
                start = index
                end = lis2[index + 1][1]
                tot -= lis2[index + 1][3]
                tot_len = lis2[index + 1][2] + 1
                tot += tot_len // k
                lis2[end] = [start, end, tot_len, tot_len // k]
                lis2[start] = lis2[end]
            else:
                tot += 1 // k
                lis2[index] = [index, index, 1, 1 // k]
            if(tot >= m):
                return val
        return -1
