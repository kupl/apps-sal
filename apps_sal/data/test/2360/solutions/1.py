t = int(input())
ans1 = []
for i in range(t):
    n = int(input())
    st = []
    for i in range(n):
        l, r = map(int, input().split())
        st.append((l, r, i))
    st = sorted(st, key=lambda x: (x[0], x[2]))
    ans = []
    f = -1
    for s in st:
        if s[1] < f:
            ans.append(0)
        else:
            ans.append(max(f, s[0]))
            f = ans[-1] + 1
    ans1.append(ans)
for ans2 in ans1:
    print(' '.join([str(i) for i in ans2]))
