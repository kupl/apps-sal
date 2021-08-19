q = int(input())
for i in range(q):
    (a, b) = list(map(int, input().split()))
    print((a - 1) * 9 + b)
