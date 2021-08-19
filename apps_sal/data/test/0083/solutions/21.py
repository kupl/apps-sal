n = int(input())
a = [int(t) for t in input().split(' ')]
plus = len([t for t in a if t > 0])
minus = len([t for t in a if t < 0])
if plus >= n // 2 + n % 2:
    print(1)
elif minus >= n // 2 + n % 2:
    print(-1)
else:
    print(0)
