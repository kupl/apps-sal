def count():
    ans = 0
    if not r % 2:
        ans += 1
    if not g % 2:
        ans += 1
    if not b % 2:
        ans += 1
    if not w % 2:
        ans += 1
    return ans


for nt in range(int(input())):
    r, g, b, w = map(int, input().split())
    if count() >= 3:
        print("Yes")
        continue
    if min(r, g, b) > 0:
        r -= 1
        g -= 1
        b -= 1
        w += 3
        if count() >= 3:
            print("Yes")
        else:
            print("No")
        continue
    print("No")
