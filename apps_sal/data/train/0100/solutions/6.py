t = int(input())
for i in range(t):
    (r, g, b) = list(map(int, input().split()))
    maxi = max(r, g, b)
    total = r + g + b
    if 2 * maxi > total:
        print(total - maxi)
    else:
        print(total // 2)
