(x, y) = map(int, input().split())
n = int(input())
f = [x, y, y - x, -x, -y, x - y]
print(f[(n - 1) % len(f)] % 1000000007)
