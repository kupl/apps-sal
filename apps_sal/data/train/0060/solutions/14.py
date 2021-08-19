t = int(input())
for _ in range(t):
    (a, b) = list(map(int, input().split()))
    x = a & b
    print((a ^ x) + (b ^ x))
