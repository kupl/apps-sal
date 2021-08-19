N = int(input())
ans = 0
res = 1
for i in range(2, N + 1):
    j = i
    if j % 2 == 1:
        continue
    cnt = 0
    while j % 2 == 0:
        j //= 2
        cnt += 1
    if ans < cnt:
        res = i
        ans = cnt
print(res)
