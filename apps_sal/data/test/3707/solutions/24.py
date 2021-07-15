n, t, k, d = list(map(int, input().split()))
cakes = ((d + t) // t) * k
if cakes < n:
    print("YES")
else:
    print("NO")

