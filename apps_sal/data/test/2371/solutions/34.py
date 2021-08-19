(n, z, w) = map(int, input().split())
a = [w] + list(map(int, input().split()))
print(max(abs(a[-1] - w), abs(a[-2] - a[-1])))
