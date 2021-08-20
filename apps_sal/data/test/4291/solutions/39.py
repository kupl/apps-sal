(N, Q) = [int(i) for i in input().split()]
S = input()
cs = [0]
for i in range(1, N):
    if S[i - 1] + S[i] == 'AC':
        cs.append(cs[i - 1] + 1)
    else:
        cs.append(cs[i - 1])
for (l, r) in ([int(i) for i in input().split()] for _ in range(Q)):
    print(cs[r - 1] - cs[l - 1])
