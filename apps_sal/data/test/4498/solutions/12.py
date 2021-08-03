a, b, c, d = map(int, input().split())

# a<b<c
ba = abs(b - a)
cb = abs(c - b)
ca = abs(c - a)

if ca <= d:
    print("Yes")
elif ba <= d and cb <= d:
    print("Yes")
else:
    print("No")
