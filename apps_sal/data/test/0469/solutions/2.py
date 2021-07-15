r, h = map(int, input().split())
h *= 2
if h < r:
    print(1)
    return
r *= 2
ans = (h + r // 2) // r * 2
h -= r * (ans // 2 - 1)
if (h ** 2) * 4 >= (r ** 2) * 3:
    ans += 1
print(ans)
