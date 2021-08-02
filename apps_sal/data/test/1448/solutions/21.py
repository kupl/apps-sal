n, d = list(map(int, input().split()))
m = int(input())

for _ in range(m):
    x, y = list(map(int, input().split()))
    first = y <= x + d
    second = y >= x - d
    third = y >= -x + d
    fourth = y <= -x + 2 * n - d

    if first and second and third and fourth:
        print("YES")
    else:
        print("NO")
