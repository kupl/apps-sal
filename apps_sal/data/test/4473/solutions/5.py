t = int(input())
for i in range(t):
    a, b, k = map(int, input().split())
    n = k // 2
    mod = k % 2
    print(n * (a - b) + mod * a)
