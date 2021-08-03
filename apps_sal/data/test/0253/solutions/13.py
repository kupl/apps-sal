k1, k2, k3 = list(map(int, input().split()))
L = [k1, k2, k3]


if L.count(1) != 0:
    print("YES")
elif L.count(2) >= 2:
    print('YES')

elif L.count(3) == 3:
    print("YES")

elif L.count(4) == 2 and L.count(2) == 1:
    print("YES")
else:
    print("NO")
