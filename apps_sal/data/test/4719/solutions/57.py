m = 10**9
n = int(input())
a = 'abcdefghijklmnopqrstuvwxyz'
pue = []
for i in range(len(a)):
    pue.append([a[i], m])
for i in range(n):
    s = input()
    for j in range(26):
        pue[j][1] = min(s.count(a[j]), pue[j][1])

ans = ''
for i in range(26):
    for j in range(pue[i][1]):
        ans += a[i]
print(ans)
