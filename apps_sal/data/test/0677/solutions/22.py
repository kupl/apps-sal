n = int(input())
for i in range(n):
    (a, b, c) = list(map(int, input().split()))
    if a > c:
        print(c)
    else:
        print((b + c) // c * c)
