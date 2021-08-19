(n, a, b) = list(map(int, input().split()))
ans = 0
for i in range(1, n + 1):
    temp = 0
    c = str(i)
    for j in range(len(c)):
        temp += int(c[j])
    if a <= temp and temp <= b:
        ans += i
print(ans)
