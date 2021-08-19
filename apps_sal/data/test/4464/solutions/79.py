(a, b, c) = list(map(int, input().split()))
ans = 'NO'
for i in range(0, b + 1):
    for j in range(0, a + 1):
        if a * i == b * j + c:
            ans = 'YES'
            break
print(ans)
