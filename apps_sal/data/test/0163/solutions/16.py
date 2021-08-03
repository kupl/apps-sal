n, k = list(map(int, input().split()))
s = input()
g = s.index("G")
t = s.index("T")
if (g > t):
    g, t = t, g
if (t - g) % k:
    print("NO")
elif "#" in s[g + k:t:k]:
    print("NO")
else:
    print("YES")
