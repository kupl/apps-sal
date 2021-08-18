
from sys import stdin, stdout


def main():
    n = int(stdin.readline())
    a = [int(i) for i in stdin.readline().split()]
    d = dict()
    for v in a:
        v3 = 0
        vc = v
        while vc % 3 == 0:
            vc = vc // 3
            v3 += 1
        temp = d.get(v3, [])
        temp.append(v)
        d[v3] = temp
    k = list(d.keys())
    k.sort()
    k.reverse()
    out = []
    for i in k:
        temp = d[i]
        temp.sort()
        out += temp
    stdout.write(" ".join([str(i) for i in out]) + "\n")


main()
