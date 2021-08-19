def mi():
    return list(map(int, input().split()))


n = int(input())
ma = -1
while n:
    n -= 1
    (a, b) = mi()
    ma = max(ma, a + b)
print(ma)
