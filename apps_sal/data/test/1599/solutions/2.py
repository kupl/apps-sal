c = ''
d = [0]
for i in input():
    if i == c:
        d.append(d[-1] + 1)
    else:
        d.append(d[-1])
    c = i
for i in range(int(input())):
    (l, r) = map(int, input().split())
    print(d[r] - d[l])
