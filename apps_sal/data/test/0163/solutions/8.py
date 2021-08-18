n, k = [int(item) for item in input().split()]
s = list(input())

g = s.index("G")
t = s.index("T")
v = 0
if g < t:
    v = k
else:
    v = -k
i = g
while i >= 0 and i < n:
    if i == t:
        print("YES")
        break
    elif s[i] == "
    print("NO")
    break
    i += v
else:
    print("NO")
