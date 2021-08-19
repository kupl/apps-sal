(N, A, B) = list(map(int, input().split()))
ans = 0
for i in range(N + 1):
    i = str(i)
    count = 0
    for j in i:
        count += int(j)
    if A <= count and B >= count:
        ans += int(i)
print(ans)
