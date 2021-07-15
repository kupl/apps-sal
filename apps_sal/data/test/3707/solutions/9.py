n, t, k, d = map(int, input().split())
t1 = ((n + k - 1) // k) * t
if t1 <= d:
    print("NO")
elif ((n - 1) // k) * t > d:
    print("YES")
else:
    print("NO")
