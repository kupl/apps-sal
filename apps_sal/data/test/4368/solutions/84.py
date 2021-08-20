(n, k) = map(int, input().split())
ans = []
while n > 0:
    ans.append(n % k)
    n /= k
    n = int(n)
print(len(ans))
