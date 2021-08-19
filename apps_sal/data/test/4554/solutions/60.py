(w, a, b) = map(int, input().split())
aw = a + w
bw = b + w
if a == bw or b == aw or a == b:
    print(0)
elif a < b < aw or b < a < bw:
    print(0)
else:
    if aw < b:
        print(b - aw)
    if bw < a:
        print(a - bw)
