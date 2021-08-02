N = int(input())
inc = []
dec = []
for i in range(N):
    a, b = map(int, input().split())
    if a < b:
        inc.append((a, b, i + 1))
    else:
        dec.append((a, b, i + 1))
inc.sort(key=lambda x: x[1], reverse=True)
dec.sort(key=lambda x: x[1])
if len(inc) >= len(dec):
    print(len(inc))
    for i in inc:
        print(i[2], end=' ')
else:
    print(len(dec))
    for i in dec:
        print(i[2], end=' ')
