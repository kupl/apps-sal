"""
NTC here
"""


def iin(): return int(input())


def lin(): return list(map(int, input().split()))


def main():
    from bisect import bisect_right as br, bisect_left as bl
    t = iin()
    while t:
        t -= 1
        n, k = lin()
        x = lin()
        y = lin()
        x.sort()
        sol = []
        for i in range(n):
            val = x[i] + k
            pos = br(x, val)
            sol.append([x[i], pos - i])
        # print(sol)
        s1 = [i for i, j in sol]
        a1 = [j for i, j in sol]
        for i in range(n - 2, -1, -1):
            a1[i] = max(a1[i], a1[i + 1])
        # print(a1, s1)
        ans = max(sol, key=lambda x: x[1])[1]
        for i in range(n):
            val, count = sol[i]
            pos = bl(s1, val + k + 1)
            if pos < n:
                # print(count, a1[pos], ans)
                ans = max(count + a1[pos], ans)
        print(ans)


main()
