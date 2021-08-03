x, y, z, t1, t2, t3 = list(map(int, input().split()))
stair = t1 * abs(x - y)
lift = t2 * (abs(z - x) + abs(x - y)) + t3 * 3
print("YES" if lift <= stair else "NO")
