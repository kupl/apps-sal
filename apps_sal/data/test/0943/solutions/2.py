n = int(input())
a = sorted(list(map(int, input().split())))[::-1]
t = r = 0
for x in a:
    if x % 2:
        if t:
            r += t + x
            t = 0
        else:
            t = x
    else:
        r += x
print(r)
