N, Q = map(int, input().split())
S = input()
ls = [0]
for i in range(N - 1):
    if S[i] == 'A' and S[i + 1] == 'C':
        ls.append(ls[i] + 1)
    else:
        ls.append(ls[i])

for i in range(Q):
    l, r = map(int, input().split())
    print(ls[r - 1] - ls[l - 1])
