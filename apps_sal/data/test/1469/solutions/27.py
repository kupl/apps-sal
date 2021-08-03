L = int(input())

b = bin(L - 1)[2:]
l = len(b)
out = []
for i in range(1, l + 1):
    out.append([i, i + 1, 0])
for i in range(2, l + 1):
    out.append([i, i + 1, 1 << (l - i)])

if not "0" in b:
    out.append([1, 2, 1 << (l - 1)])
    b = ""
while len(b) > 0 and b != "0":
    if b[-1] == "0":
        out.append([1, len(b) + 1, int((b + "0" * l)[:l], 2)])
        b = bin(int(b, 2) - 1)[2:]
    b = b[:-1]

if l < 20:
    print(l + 1, len(out))
    for sub in out:
        print(" ".join(map(str, sub)))
else:
    print(l, len(out) - 1)
    for u, v, w in out[1:]:
        u = max(1, u - 1)
        v = max(1, v - 1)
        print(u, v, w)
