N = int(input())
a = list(map(int, input().split()))
cnt = 0
for i in range(len(a)):
    if i + 1 - cnt != a[i]:
        cnt += 1
if cnt == N:
    print(-1)
else:
    print(cnt)
