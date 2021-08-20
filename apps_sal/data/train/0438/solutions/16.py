class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        len_arr = len(arr)
        tot = 0
        latest = -1
        i1 = 0
        lis = [[] for x in range(len_arr)]
        for i in arr:
            index = i - 1
            if index > 0 and lis[index - 1] and (index < len_arr - 1) and lis[index + 1]:
                if lis[index - 1][2] == m:
                    tot -= 1
                if lis[index + 1][2] == m:
                    tot -= 1
                start = lis[index - 1][0]
                end = lis[index + 1][1]
                lis1 = [start, end, lis[index - 1][2] + 1 + lis[index + 1][2]]
                if lis1[2] == m:
                    tot += 1
                lis[start] = lis1
                lis[end] = lis1
            elif index > 0 and lis[index - 1]:
                if lis[index - 1][2] == m:
                    tot -= 1
                start = lis[index - 1][0]
                end = index
                if lis[index - 1][2] + 1 == m:
                    tot += 1
                lis1 = [start, end, lis[index - 1][2] + 1]
                lis[start] = lis1
                lis[end] = lis1
            elif index < len_arr - 1 and lis[index + 1]:
                if lis[index + 1][2] == m:
                    tot -= 1
                start = index
                end = lis[index + 1][1]
                if lis[index + 1][2] + 1 == m:
                    tot += 1
                lis1 = [start, end, lis[index + 1][2] + 1]
                lis[end] = lis1
                lis[start] = lis1
            else:
                lis[index] = [index, index, 1]
                if m == 1:
                    tot += 1
            if tot > 0:
                latest = i1 + 1
            i1 += 1
        return latest
