def solve(a, b, c):
    (x, y) = (c // a, c // b)
    for i in range(x + 1):
        for j in range(y + 1):
            if a * i + b * j == c:
                return True
    return False


(a, b, c) = list(map(int, input().split()))
if solve(a, b, c):
    print('Yes')
else:
    print('No')
