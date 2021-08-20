n = int(input())
a = list(map(int, input().split()))
odd = [a[i] for i in range(n) if i % 2 == 1]
even = [a[j] for j in range(n) if j % 2 == 0]
if n % 2 == 0:
    ans = list(reversed(odd)) + even
else:
    ans = list(reversed(even)) + odd
print(*ans)
