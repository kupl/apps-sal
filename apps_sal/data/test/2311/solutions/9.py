import sys
input = sys.stdin.readline
n, m, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
scale = 40000
#scale = 10
ca = [0 for _ in range(scale + 1)]
cb = [0 for _ in range(scale + 1)]
now = 0
for x in a:
    if x:
        now += 1
    else:
        now = 0
    ca[now] += 1
now = 0
for x in b:
    if x:
        now += 1
    else:
        now = 0
    cb[now] += 1
# print(ca)
# print(ca)
for i in range(scale)[::-1]:
    ca[i] += ca[i + 1]
    cb[i] += cb[i + 1]
# print(ca)
# print(cb)
ans = 0
roo = int(k**.5)
for i in range(1, roo + 1):
    if k % i == 0 and k // i <= scale:
        ans += ca[i] * cb[k // i]
        ans += cb[i] * ca[k // i]
if roo ** 2 == k:
    ans -= ca[roo] * cb[roo]
print(ans)
