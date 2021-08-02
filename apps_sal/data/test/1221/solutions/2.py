class Solution:
    def resolve(self, n, m, a, b):
        prod = [0] * n
        for i, ai in enumerate(a):
            mm = ai * b[0]
            for bi in b:
                mm = max(mm, ai * bi)
            prod[i] = mm
        prod.sort()
        return prod[-2]


def __starting_point():
    s = Solution()

    n, m = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    re = s.resolve(n, m, a, b)
    print(re)


__starting_point()
