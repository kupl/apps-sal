from collections import defaultdict


class Solution:

    def getWinner(self, arr, k):
        r = []
        i = 0
        n = len(arr)
        z = defaultdict(int)
        while True:
            arr += r
            n = len(arr)
            while i < n - 1:
                j = i + 1
                if arr[j] > arr[i]:
                    z[arr[j]] += 1
                    if z[arr[j]] == k:
                        return arr[j]
                    q = arr[j]
                    r.append(arr.pop(i))
                else:
                    z[arr[i]] += 1
                    if z[arr[i]] == k:
                        return arr[i]
                    q = arr[i]
                    r.append(arr.pop(j))
                n = len(arr)
                if n == 1:
                    return q
                for p in z:
                    if p != q:
                        z[p] = 0
