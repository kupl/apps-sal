import sys
readline = sys.stdin.readline
T = int(readline())
Ans = [None] * T
for qu in range(T):
    (N, K) = list(map(int, readline().split()))
    S = [1 if s == 'W' else 0 for s in readline().strip()]
    if all((s == 0 for s in S)):
        Ans[qu] = max(0, 2 * K - 1)
        continue
    ans = 0
    ctr = 0
    st = []
    L = []
    res = 0
    hh = False
    for i in range(N):
        s = S[i]
        if s == 1:
            if i == 0 or S[i - 1] == 0:
                ans += 1
            else:
                ans += 2
            if ctr:
                st.append(ctr)
                ctr = 0
            hh = True
        elif hh:
            ctr += 1
        else:
            res += 1
    res += ctr
    st.sort()
    J = []
    for s in st:
        J.extend([2] * (s - 1) + [3])
    J.extend([2] * res)
    Ans[qu] = ans + sum(J[:min(len(J), K)])
print('\n'.join(map(str, Ans)))
