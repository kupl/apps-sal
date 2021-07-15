from collections import Counter

cnt = Counter(input().strip())
vals = sorted(cnt.values())

if len(vals) == 1 or len(vals) > 4:
    print("No")
elif len(vals) == 2:
    a, b = vals
    if a == 1:
        print("No")
    else:
        print("Yes")
elif len(vals) == 3:
    a, b, c = vals
    if c == 1:
        print("No")
    else:
        print("Yes")
elif len(vals) == 4:
    print("Yes")
else:
    raise RuntimeError("Should never happen")

