def main():
    a = open('input.txt', 'r')
    c = open('output.txt', 'w')
    b = a.readline().split()
    n = int(b[0])
    k = int(b[1])
    b = a.readline().split()
    h = []
    d = []
    for i in range(len(b)):
        h.append((int(b[i]), i + 1))
    h.sort()
    for i in range(1, k + 1):
        d.append(h[-i])
    d.sort()
    e = str(d[0][0])
    c.write('{0}\n' .format(e))
    f = []
    for i in range(len(d)):
        f.append(d[i][1])
    f.sort()
    for i in range(len(f)):
        g = str(f[i])
        c.write(g + " ")


main()
