import math
import collections


class Solution:

    def threeSumMulti(self, A: List[int], target: int) -> int:
        c1 = collections.Counter(A)
        arr = []
        triples = set()
        for i in sorted(c1.keys()):
            arr += [i] * min(3, c1[i])
        for i in range(len(arr) - 2):
            j = i + 1
            k = len(arr) - 1
            twoSum = target - arr[i]
            while j < k:
                tmp = arr[j] + arr[k]
                if tmp == twoSum:
                    triples.add((arr[i], arr[j], arr[k]))
                    k -= 1
                elif tmp >= twoSum:
                    while k - 1 > 0 and arr[k - 1] == arr[k]:
                        k -= 1
                    k -= 1
                else:
                    while j + 1 < len(arr) - 1 and arr[j + 1] == arr[j]:
                        j += 1
                    j += 1
        tot = 0
        mod = 10 ** 9 + 7
        for t in triples:
            c2 = collections.Counter(t)
            combs = 1
            for k in list(c2.keys()):
                combs *= math.comb(c1[k], c2[k])
                combs %= mod
            tot += combs
            tot %= mod
        return tot
