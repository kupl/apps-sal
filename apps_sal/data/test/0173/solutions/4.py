# CF BAYAN WARMUP
# B

l = input()
h = input()
v = input()

if h[0] == "<" and v[0] == "^":
    print("NO")
elif h[0] == ">" and v[-1] == "^":
    print("NO")
elif h[-1] == "<" and v[0] == "v":
    print("NO")
elif h[-1] == ">" and v[-1] == "v":
    print("NO")
else:
    print("YES")

