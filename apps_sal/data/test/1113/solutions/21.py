input()
a = tuple(map(int, input().split()))
top = -1
for i, x in enumerate(a, start=1):
    if x - top <= 1:
        top = max(x, top)
    else:
        print(i)
        return
print(-1)

