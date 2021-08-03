def solve():
    N = int(input())
    S = input()

    def rolling_hash(s, mod, base=37):
        l = len(s)
        h = [0] * (l + 1)
        v = 0
        for i in range(l):
            h[i + 1] = v = (v * base + ord(s[i])) % mod
        pw = [1] * (l + 1)
        v = 1
        for i in range(l):
            pw[i + 1] = v = v * base % mod
        return h, pw

    def chk(S, mod, D=[0] * N):
        h, pw = rolling_hash(S, mod)
        left = 0
        right = N // 2 + 1
        while left + 1 < right:
            l = mid = (left + right) >> 1
            p = pw[l]
            for i in range(min(l, N - 2 * l + 1)):
                D[i] = (h[l + i] - h[i] * p) % mod
            s = set()
            ok = 0
            for i in range(l, N - l + 1):
                s.add(D[i - l])
                D[i] = v = (h[l + i] - h[i] * p) % mod
                if v in s:
                    ok = 1
                    break
            if ok:
                left = mid
            else:
                right = mid
        return left

    print((chk(S, 10**9 + 9)))


solve()
