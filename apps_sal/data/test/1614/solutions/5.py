n, h = list(map(int, input().split()))
a = list(map(int, input().split()))
w = 0
for k in a:
    if k > h:
        w += 2
    else:
        w += 1
print(w)
