n = int(input())
s = [int(input()) for i in range(n)]
st = sorted(s)
ans = [0]
sm1 = sum(s)
for i in range(len(st)):
    if sm1 % 10 != 0:
        ans.append(sm1)
        break
    else:
        sm1 -= st[i]
sm2 = sum(s)
for i in range(len(st)):
    if st[i] % 10 != 0:
        ans.append(sm2 - st[i])
        break
print(max(ans))
