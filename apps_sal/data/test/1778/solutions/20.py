def I(): return map(int, input().split())


n = int(input())
a = sorted(list(I()))
b = sorted(list(I()))
sa = sb = 0
for i in range(2 * n):
    if i % 2 == 0:
        if len(a) > 0 and len(b) > 0 and a[-1] > b[-1]:
            sa += a[-1]
            del a[-1]
        elif len(b) > 0:
            del b[-1]
        else:
            sa += a[-1]
            del a[-1]
    else:
        if len(a) > 0 and len(b) > 0 and b[-1] > a[-1]:
            sb += b[-1]
            del b[-1]
        elif len(a) > 0:
            del a[-1]
        else:
            sb += b[-1]
            del b[-1]
print(sa - sb)
