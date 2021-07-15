n, h = list(map(int, input().split()))
a = list(map(int, input().split()))

w = 0

for friend in a:
    if friend <= h:
        w += 1
    else:
        w += 2
print(w)

