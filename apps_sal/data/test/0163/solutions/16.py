n, k = list(map(int, input().split()))
s = input()
g = s.index("G")
t = s.index("T")
if (g > t):
    g, t = t, g
if (t - g) % k:
    print("NO")
elif "
print("NO")
else:
    print("YES")
