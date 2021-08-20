(a, b) = list(map(int, input().split()))
ans = 100000000000
if a == 0:
    print(0)
else:
    for i in range(1, b):
        if a % i == 0:
            ans = min(a // i * b + i, ans)
print(ans)
