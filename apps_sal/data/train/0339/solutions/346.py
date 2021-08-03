from collections import defaultdict


class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        dic1 = defaultdict(list)
        dic2 = defaultdict(list)
        for idx, i in enumerate(nums1):
            dic1[i].append(idx)
        for idx, i in enumerate(nums2):
            dic2[i].append(idx)
        count = 0
        for i in nums1:
            sq = i * i
            for j in set(nums2):
                ano = sq / j
                # print(\"ano,\", ano, sq, j)
                if ano != int(ano):
                    continue
                ano = int(ano)
                if ano in dic2:
                    inc = 0
                    if ano == j:
                        inc += int(len(dic2[ano]) * (len(dic2[ano]) - 1) / 2)
                    else:
                        inc += len(dic2[ano]) * len(dic2[j]) / 2
                    count += inc
                    # print(\"i is\", i, \" inc\", inc)
        for i in nums2:
            sq = i * i
            for j in set(nums1):
                ano = sq / j
                if ano != int(ano):
                    continue
                ano = int(ano)
                if ano in dic1:
                    inc = 0
                    if ano == j:
                        inc += int(len(dic1[ano]) * (len(dic1[ano]) - 1) / 2)
                    else:
                        inc += len(dic1[ano]) * len(dic1[j]) / 2
                    # print(\"i is\", i, \" inc\", inc)
                    count += inc
        return int(count)
