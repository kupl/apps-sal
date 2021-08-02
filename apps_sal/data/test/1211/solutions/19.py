R = lambda: list(map(int, input().split()))

n, m = R()

a = list(R())

ans = float('inf')
ans_i = 0

for i in range(m):
    temp = n % a[i]
    if temp < ans:
        ans = temp
        ans_i = i

print(ans_i + 1, n // a[ans_i])
