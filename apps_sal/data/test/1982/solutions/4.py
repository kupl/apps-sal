t = int(input())
for i in range(t):
    n, k = list(map(int, input().split()))
    if k ** 2 <= n and k % 2 == n % 2:
        print("YES")
    else:
        print("NO")
