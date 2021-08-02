n = int(input())
cnt = 0
ans = 'No'

for _ in range(n):
    d = list(map(int, input().split()))
    if d[0] == d[1]:
        cnt += 1
    else:
        cnt = 0

    if cnt >= 3:
        ans = 'Yes'

print(ans)
