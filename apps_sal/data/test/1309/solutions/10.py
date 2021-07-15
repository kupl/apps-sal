n = int(input())
v = [int(i) for i in input().split()]
v = sorted(v)

def dp(i, chosen):
    if chosen == 0:
        d = 0
        while i < len(v):
            d += v[i+1] - v[i]
            i += 2
        return d
    if i >= len(v) - 1:
        return 0
    return min(v[i+1] - v[i] + dp(i+2, chosen), dp(i+1, chosen-1))

print(dp(0, 2))

