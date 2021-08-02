t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    if k % 2 == 0 and n % 2 == 1:
        print("NO")
    elif (k % 2 == 1 and n % 2 == 0 and n < 2 * k) or n < k:
        print("NO")
    elif k % 2 == 1 and n % 2 == 0:
        print("YES")
        ans = [2] * (k - 1) + [n - 2 * (k - 1)]
        print(*ans)
    else:
        print("YES")
        ans = [1] * (k - 1) + [n - k + 1]
        print(*ans)
