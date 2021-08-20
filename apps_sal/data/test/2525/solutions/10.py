S = input()
N = int(input())
flg = 0
L = []
for i in range(N):
    e = input().split()
    if e[0] == '1':
        flg += 1
        flg = flg % 2
    else:
        L.append(((flg + int(e[1])) % 2, e[2]))
S = ''.join(list(reversed(S))) if flg else S
(s1, s2) = ('', '')
for (f, v) in L:
    if (flg + f) % 2 == 1:
        s1 += v
    else:
        s2 += v
ans = ''.join(list(reversed(s1))) + S + s2
print(ans)
