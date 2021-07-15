n = int(input())
a = list(map(int, input().split())) + [0]
b = list(map(int, input().split())) + [0]
a.sort()
b.sort()
sa = 0
sb = 0
while len(a) > 1 or len(b) > 1:
    if a[-1] > b[-1]:
        sa += a.pop()
    else:
        b.pop()
    if a[-1] > b[-1]:
        a.pop()
    else:
        sb += b.pop()
print(sa - sb)
