"""This code was written by
Russell Emerine - linguist,
mathematician, coder,
musician, and metalhead."""

n = int(input())
for _ in range(n):
    a, b = list(map(int, input().split()))
    if (a + b) % 3 != 0:
        print("NO")
    elif 2 * b - a < 0:
        print("NO")
    elif 2 * a - b < 0:
        print("NO")
    else:
        print("YES")
