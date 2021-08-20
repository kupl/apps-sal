(n, k) = [int(i) for i in input().split()]
s = [0] * k
for i in range(n):
    s[int(input()) - 1] += 1
p = 0
for i in s:
    p += i % 2
print(n - p // 2)
