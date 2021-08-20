n = int(input())
l = list(map(int, input().split()))
if n == 1:
    print(1)
else:
    left = [0 for i in range(n)]
    right = [0 for i in range(n)]
    left[0] = l[0]
    right[-1] = l[-1]
    left[1] = l[1]
    right[-2] = l[-2]
    for i in range(2, n):
        left[i] = left[i - 2] + l[i]
    for i in range(n - 3, -1, -1):
        right[i] = right[i + 2] + l[i]
    ans = 0
    for i in range(n):
        a = right[i + 1] if i < n - 1 else 0
        b = left[i - 2] if i >= 2 else 0
        lhs = a + b
        a = right[i + 2] if i < n - 2 else 0
        b = left[i - 1] if i >= 1 else 0
        rhs = a + b
        if lhs == rhs:
            ans += 1
    print(ans)
