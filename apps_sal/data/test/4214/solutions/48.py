def func(n):
    if n == 1:
        return 1
    return n * func(n - 1)


n = int(input())
L = [0 for i in range(n)]
for i in range(n):
    L[i] = list(map(int, input().split()))
ans = 0
for i in range(n):
    for j in range(i + 1, n):
        length = (L[i][0] - L[j][0])**2 + (L[i][1] - L[j][1])**2
        length = length**0.5
        ans += length * func(n - 1) * 2
print(ans / func(n))
