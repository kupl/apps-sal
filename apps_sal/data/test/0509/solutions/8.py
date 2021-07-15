def gen(i, angle):
    if i == n:
        return angle % 360 == 0
    return gen(i + 1, angle + a[i]) or gen(i + 1, angle - a[i])

n = int(input())
a = [int(input()) for _ in range(n)]

print("YES" if gen(0, 0) else "NO")
