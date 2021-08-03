t, s, x = list(map(int, input().split()))

if (x < t):
    print("NO")
elif (x - t) % s == 0:
    print("YES")
elif ((x - t - 1) % s == 0) and (x > t + s):
    print("YES")
else:
    print("NO")
