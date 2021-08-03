t = int(input())

for t_i in range(t):
    n = int(input())
    P = input().split()
    l, r = -1, -1
    for i in range(n):
        P[i] = int(P[i])
        if P[i] == 1:
            l = i
            r = i
    max_seen = 1
    beaut = ['1']
    for _ in range(n - 1):
        if l == 0:
            l_cand = 10**8
        else:
            l_cand = P[l - 1]
        if r == n - 1:
            r_cand = 10**8
        else:
            r_cand = P[r + 1]
        if r_cand > l_cand:
            l -= 1
            max_seen = max(l_cand, max_seen)
        else:
            r += 1
            max_seen = max(r_cand, max_seen)
        beaut.append('1' if max_seen == r - l + 1 else '0')
    print(''.join(beaut))
