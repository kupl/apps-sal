n = int(input())
for i in range(n):
    (a, b) = map(int, input().split())
    s = abs(a - b)
    x = s // 5
    s %= 5
    x += s // 2
    s %= 2
    x += s
    print(x)
