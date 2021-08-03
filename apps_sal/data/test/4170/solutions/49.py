n = int(input())
h = [int(i) for i in input().split()]
ans = 0
cnt = 0
for i in range(n - 1):
    if h[i] >= h[i + 1]:
        cnt += 1
    else:
        if ans < cnt:
            ans = cnt
        cnt = 0
if ans < cnt:
    ans = cnt
    cnt = 0
print(ans)
