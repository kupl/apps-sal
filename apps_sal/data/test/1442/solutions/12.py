(n, s) = list(map(int, input().split()))
B = []
S = []
for i in range(n):
    st = list(input().split())
    (st[1], st[2]) = (int(st[1]), int(st[2]))
    if st[0] == 'B':
        B.append(st)
    else:
        S.append(st)
B.sort()
S.sort()
i = 0
while i < len(B) - 1:
    if B[i][1] == B[i + 1][1]:
        B[i][2] += B[i + 1][2]
        del B[i + 1]
    else:
        i += 1
i = 0
while i < len(S) - 1:
    if S[i][1] == S[i + 1][1]:
        S[i][2] += S[i + 1][2]
        del S[i + 1]
    else:
        i += 1
B.reverse()
b = []
for i in range(min(s, len(S))):
    b.append(S[i])
b.reverse()
for i in range(len(b)):
    print(*b[i])
for i in range(min(s, len(B))):
    print(*B[i])
