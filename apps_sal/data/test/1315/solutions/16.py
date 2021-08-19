n = int(input())
line = [int(i) for i in input().split()]
for i in range(len(line)):
    line[i] += i
line.sort()
for i in range(len(line)):
    line[i] -= i
impossivel = False
for i in range(len(line) - 1):
    if line[i] > line[i + 1]:
        impossivel = True
        break
if impossivel:
    print(':(')
else:
    print(' '.join([str(i) for i in line]))
