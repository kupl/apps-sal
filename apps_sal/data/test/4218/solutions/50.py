n = int(input())

cnt = 0
for i in range(1, n+1):
    if i%2:
        cnt += 1

ans = cnt/n
print(ans)
