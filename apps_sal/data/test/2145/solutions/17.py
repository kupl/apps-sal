

def possible(x, y):
    if x >= 4:
        return True
    if x == 3:
        return y <= 3
    if x == 2:
        return y <= 3
    if x == 1:
        return y == 1


t = int(input())
for _ in range(t):
    a, b = [int(x) for x in input().split()]
    print("YES" if possible(a, b) else "NO")
