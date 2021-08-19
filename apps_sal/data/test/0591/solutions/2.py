fc = open('input.txt', 'r')
(n, k) = [int(x) for x in fc.readline().strip().split()]
line = fc.readline().strip().split()
b = [(int(line[i]), i + 1) for i in range(len(line))]
b.sort()
l = list()
for i in range(len(b) - k, len(b)):
    l.append(str(b[i][1]))
fw = open('output.txt', 'w')
fw.write('{0}\n'.format(b[len(b) - k][0]))
fw.write(' '.join(l))
fw.write('\n')
fc.close()
fw.close()
