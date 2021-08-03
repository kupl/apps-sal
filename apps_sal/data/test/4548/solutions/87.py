n, m, x = map(int, input().split())
li = list(map(int, input().split()))
cnt = 0
cou = 0
for i in range(x):
    if i in li:
        cnt += 1
for i in range(x, n):
    if i in li:
        cou += 1
print(min(cnt, cou))
