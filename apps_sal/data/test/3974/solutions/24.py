def solve(s):
    n = len(s)
    if(n == 1):
        return 1
    else:
        start = 0
        prev = s[0]
        ans = 0
        f = 1
        for i in range(1, n):
            f = 1
            if(s[i] == prev):
                continue
            else:
                f = 0
                ans = max(ans, i - start)
                start = i
                prev = s[i]
        if(f):
            ans = max(ans, n - start)
            start = i
            prev = s[i]
        return ans


def solve1(s):
    st = []
    ans = 0
    maxx = 0
    for i in s:
        if(st):
            ans = 0
        if(i == '+'):
            st.append('+')
        else:
            if(st):
                st.pop()
            else:
                ans += 1
                maxx = max(maxx, ans)
        maxx = max(maxx, len(st))
    maxx = max(maxx, len(st))
    return maxx


def solve2(s):
    st = []
    ans = 0
    maxx = 0
    for i in s:
        if(st):
            ans = 0
        if(i == '-'):
            st.append('-')
        else:
            if(st):
                st.pop()
            else:
                ans += 1
                maxx = max(maxx, ans)
        maxx = max(maxx, len(st))
    maxx = max(maxx, len(st))
    return maxx


l = input()
ans = solve(l)
ans1 = solve1(l)
ans2 = solve2(l)
print(max(ans, ans1, ans2))
