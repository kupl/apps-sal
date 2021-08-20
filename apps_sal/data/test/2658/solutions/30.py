(n, k) = map(int, input().split())
a = list(map(int, input().split()))
tele = [1]
went = set(tele)
now = 1
cnt = 0
flag = True
for i in range(k):
    now = a[now - 1]
    if i != k - 1 and now in went:
        tele = tele[tele.index(now):]
        cnt = i + 1
        flag = False
        break
    tele.append(now)
    went.add(now)
if flag == True:
    print(tele[-1])
else:
    k -= cnt
    cnt = k % len(tele)
    print(tele[cnt])
