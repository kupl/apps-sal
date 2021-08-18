def search(rules, m):
    ret = ['a']
    for i in range(m - 1):
        nex = []
        for r in ret:
            r0, tail = r[0], r[1:]
            for a, b in rules:
                if a == r0:
                    nex.append(b + tail)
        ret = nex
    return len(ret)


def main():
    line = [int(i) for i in input().split()]
    m, n = line[0], line[1]
    rules = []
    for i in range(n):
        line = input().split()
        line.reverse()
        rules.append(line)
    l = search(rules, m)
    print(l)


main()
