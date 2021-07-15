n, b, a = (int(x) for x in input().split())
s = [int(x) for x in input().split()]

charge = a
for ans, t in enumerate(s):
    if t:
        if charge < a and b:
            b -= 1
            charge += 1
        elif charge:
            charge -= 1
        elif b:
            b -= 1
        else:
            print(ans)
            raise SystemExit(0)
    else:
        if charge:
            charge -= 1
        elif b:
            b -= 1
        else:
            print(ans)
            raise SystemExit(0)
print(ans + 1)

