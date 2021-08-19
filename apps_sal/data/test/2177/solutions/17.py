n = int(input())
for _ in range(n):
    (a, b) = map(int, input().split())
    l = len(str(b))
    if len(str(b + 1)) == l + 1:
        l += 1
    print(a * (l - 1))
