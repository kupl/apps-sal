v = list(map(int, input().split()))
v.sort()
if (v[0] == 1):
    print("YES")
    return
if (v[0] == 2 and v[1] == 2):
    print("YES")
    return
if (v.count(3) == 3):
    print("YES")
    return
if (v[0] == 2 and v.count(4) == 2):
    print("YES")
    return
print("NO")
