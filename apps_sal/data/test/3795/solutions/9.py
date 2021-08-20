n = int(input())
d = int(input())
e = int(input())
ans = n % d
for i in range(100000):
    if 5 * e * i <= n:
        k = n - 5 * e * i
        if ans > k % d:
            ans = k % d
print(ans)
