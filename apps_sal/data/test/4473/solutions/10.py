t = int(input())
for i in range(t):
    a, b, k = map(int, input().split())
    print(a * (k // 2 + k % 2) - b * (k // 2))
