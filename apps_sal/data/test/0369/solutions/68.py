N, M = map(int, input().split())
S = input()

p = N
ans = []
ans_ok = True
while True:
    if p <= M:
        ans.append(p)
        p -= p
        break
    check = False
    for i in range(M, 0, -1):
        if S[p - i] == '0':
            check = True
            ans.append(i)
            p -= i
            break
    if not check:
        ans_ok = False
        break
if ans_ok:
    print(' '.join(map(str, ans[::-1])))
else:
    print(-1)
