t = int(input())
for _ in range(t):
    a, b = list(map(int, input().split()))
    i, j = 0, 9
    while j <= b:
        i += 1
        j *= 10
        j += 9
    print(a*i)

