(n, k) = map(int, input().split())
lis = []
ans = 1000000000000000000
for _ in range(n):
    lis.append(int(input()))
lis.sort()
for i in range(n):
    if i + k - 1 >= len(lis):
        break
    else:
        mi = abs(lis[i] - lis[i + k - 1])
        ans = min(ans, mi)
print(ans)
