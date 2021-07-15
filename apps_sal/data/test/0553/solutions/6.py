import sys

def distance(s, t):
    ans = 0
    for (x, y) in zip(s, t):
        ans += (x != y)
    return ans

def min_distance(n):
    codes = [line.rstrip() for line in sys.stdin]
    m = 6
    for i in range(n):
        for j in range(i+1, n):
            d = distance(codes[i], codes[j])
            if m > d:
                m = d
                if d < 3:
                    return 1
    return m

n = int(input())
if n == 1:
    print(6)
else:
    print((min_distance(n) + 1) // 2 - 1)

