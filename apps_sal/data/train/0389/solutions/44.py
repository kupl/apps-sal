class Solution:
    def splitArraySameAverage(self, A: List[int]) -> bool:
        su = sum(A)
        ii = len(A) // 2 + 1
        arr = [set() for _ in range(ii)]
        arr[0].add(0)
        for x in A:
            for t in reversed(range(1, ii)):
                arr[t] |= set(map(lambda s: s + x, arr[t - 1]))
        # print(arr)
        for i in range(1, len(A) // 2 + 1):
            if (su * i) % len(A) == 0:
                # print(i, su*i, arr[i])
                if (su * i) // len(A) in arr[i]:
                    return True
        return False
