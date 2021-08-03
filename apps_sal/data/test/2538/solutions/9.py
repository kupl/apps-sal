T = int(input())
for _ in range(T):
    a, b, c = list(map(int, input().split()))
    print(max(c + 1 - max((-a + b + c + 2) // 2, 0), 0))
