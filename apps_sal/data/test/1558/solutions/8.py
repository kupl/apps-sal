first = input().split()
n = int(first[0])
r = int(first[1])
avg = int(first[2])
marks = {}
total = 0
essays = []
for i in range(n):
    inp = input().split()
    inp[0] = int(inp[0])
    inp[1] = int(inp[1])
    total += inp[0]
    essays.append(inp[1])
    if inp[1] in marks:
        marks[inp[1]].append(inp[0])
    else:
        marks[inp[1]] = [inp[0]]

if total/n >= avg:
    print(0)
else:
    out = 0
    essays = list(set(essays))
    essays.sort()
    deficit = avg * n - total
    ind = 0
    while deficit > 0:
        current = essays[ind]
        for i in range(len(marks[current])):
            if marks[current][i] < r:
               x = r - marks[current][i]
               if deficit >= x:
                   out += current * x
                   deficit -= x
               else:
                   out += current * deficit
                   deficit = 0
               if deficit == 0:
                   break
        ind += 1
    print(out)
                

