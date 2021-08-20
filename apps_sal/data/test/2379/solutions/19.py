(n, k, c) = list(map(int, input().split()))
s = str(input())
l = []
r = []
cnt = 0
for i in range(k):
    if s[cnt] == 'o':
        l.append(cnt + 1)
        cnt += c + 1
    else:
        while s[cnt] != 'o':
            cnt += 1
        l.append(cnt + 1)
        cnt += c + 1
cnt = 1
for i in range(k):
    if s[-cnt] == 'o':
        r.append(n - cnt + 1)
        cnt += c + 1
    else:
        while s[-cnt] != 'o':
            cnt += 1
        r.append(n - cnt + 1)
        cnt += c + 1
r = r[::-1]
for i in range(k):
    if l[i] == r[i]:
        print(l[i])
