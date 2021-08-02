
def main():

    s = input()
    t = input()
    n = len(s)

    ans = 0
    for i in range(n):
        for j in range(i, n):
            a = s[: i]
            b = s[j + 1:]
            st = a + b
            cur, ok = 0, 0

            for ch in st:
                if ch == t[cur]:
                    cur += 1
                if cur == len(t):
                    ok = 1
                    break

            if ok == 1:
                ans = max(ans, len(s) - len(st))
    return ans


print(main())
