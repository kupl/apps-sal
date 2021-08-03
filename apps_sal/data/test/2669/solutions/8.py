n = int(input())
start = [int(x) for x in input().split()]
end = [int(x) for x in input().split()]

output = [0]

pos = end[0]

for i in range(1, len(start)):

    if start[i] >= pos:
        output.append(i)
        pos = end[i]


c = ' '.join([str(elem) for elem in output])
print(c)
