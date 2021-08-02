import math


def main():
    n, k = [int(i) for i in input().split()]
    l = [int(i) for i in input().split()]
    l2 = [l[i] - i * k for i in range(len(l))]
    d = dict()
    m = 0
    mn = 0
    for i in l2:
        if i > 0:
            try:
                d[i] += 1
            except:
                d[i] = 1
            if d[i] > m:
                m = d[i]
                mn = i
    count = 0
    ans = []
    for i in range(len(l2)):
        if l2[i] != mn:
            ans += [('+' if l2[i] < mn else '-') + ' ' + str(i + 1) + ' ' + str(abs(l2[i] - mn))]
            count += 1
    print(count)
    for i in ans:
        print(i)


def __starting_point(): main()


__starting_point()
