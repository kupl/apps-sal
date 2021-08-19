t = int(input())
for i in range(t):
    n = int(input())
    (r, p, s) = list(map(int, input().split()))
    st = input()
    rr = st.count('R')
    pp = st.count('P')
    ss = st.count('S')
    w = -(-n // 2)
    if min(r, ss) + min(s, pp) + min(p, rr) >= w:
        print('YES')
        ANS = ['n'] * n
        for j in range(n):
            if r > 0 and st[j] == 'S':
                ANS[j] = 'R'
                r -= 1
            elif p > 0 and st[j] == 'R':
                ANS[j] = 'P'
                p -= 1
            elif s > 0 and st[j] == 'P':
                ANS[j] = 'S'
                s -= 1
        for j in range(n):
            if ANS[j] == 'n':
                if r > 0:
                    ANS[j] = 'R'
                    r -= 1
                elif p > 0:
                    ANS[j] = 'P'
                    p -= 1
                elif s > 0:
                    ANS[j] = 'S'
                    s -= 1
        print(''.join(ANS))
    else:
        print('NO')
