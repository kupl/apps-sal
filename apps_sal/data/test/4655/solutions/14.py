Q = int(input())
for _ in range(Q):
    a, b, c = list(map(int, input().split()))
    print((a + b + c) // 2)
