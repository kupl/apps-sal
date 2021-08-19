import sys


def input():
    return sys.stdin.readline().strip()


def input_l():
    return map(int, input().split())


def input_t():
    return tuple(input_l())


def main():
    (a, s, d) = input_l()
    q = []
    e = []
    z = [0] * (a + 1)
    for i in range(s):
        w = input_t()
        for k in range(w[0], w[1]):
            q.append(k + 1)
    for j in range(d):
        e.append(input_t())
    e = sorted(e, key=lambda x: x[0])
    if e[0][0] > q[0] - 1:
        print(-1)
        return
    for i in range(1, len(z)):
        if i not in q:
            z[i] = z[i - 1]
            continue
        for j in e:
            if i >= j[0]:
                c = (i - j[0]) * j[1] + z[j[0]]
                if z[i] > 0:
                    if c < z[i]:
                        z[i] = c
                else:
                    z[i] = c
    print(z[-1])


main()
