q = int(input())
minimum = 0
maximum = -1
d = {}
for i in range(q):
    a, b = input().split()
    b = int(b)
    if a == 'L':
        minimum -= 1
        d[b] = minimum
    elif a == 'R':
        maximum += 1
        d[b] = maximum
    elif a == '?':
        print(min(d[b] - minimum, maximum - d[b]))
        

