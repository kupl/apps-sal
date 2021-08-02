t, s, x = list(map(int, input().split()))
x -= t
if x < 0:
    print("NO")
elif x % s == 0:
    print("YES")
elif x % s == 1 and x != 1:
    print("YES")
else:
    print("NO")
