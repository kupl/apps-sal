n = int(input())
for i in range(n):
    (a, b, c, d) = list(map(int, input().split()))
    if a != c:
        print(a, c)
    else:
        print(a, d)
