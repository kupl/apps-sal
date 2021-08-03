# 44 C - pushpush AC
n = int(input())
a = list(map(int, input().split()))

odd = [a[i] for i in range(n) if i % 2 == 1]  # O(n)
even = [a[j] for j in range(n) if j % 2 == 0]  # O(n)

if n % 2 == 0:
    ans = list(reversed(odd)) + even  # O(n)
else:
    ans = list(reversed(even)) + odd  # O(n)
print(*ans)
