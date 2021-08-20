(n, x) = map(int, input().split())
m = [0] * n
for i in range(n):
    m[i] = int(input())
    x -= m[i]
print(n + x // min(m))
