n = int(input())
start = [int(x) for x in input().split()]
end = [int(x) for x in input().split()]

out = [0]

pos = end[0]

for i in range(1, len(start)):

    if start[i] >= pos:
        out.append(i)
        pos = end[i]


x = ' '.join([str(elem) for elem in out])
print(x)
