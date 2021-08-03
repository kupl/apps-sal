def solve(a, t1, t2):
    l1 = t1 - (t1 - 300) % a + a
    if (l1 < 300):
        l1 = 300
    l2 = t2 - (t2 - 300) % a
    if (l2 > 1439):
        l2 = 1439
    if (l2 < l1):
        return 0
    return (l2 - l1) // a + 1 - (l2 == t2)


def trans(h, m):
    return 60 * h + m


data1 = [int(x) for x in input().split()]
data2 = [int(x) for x in input().split()]
data3 = input()
h0 = int(data3[0:2])
m0 = int(data3[-2:])
t0 = trans(h0, m0)
sol = solve(data2[0], t0 - data2[1], t0 + data1[1])
print(sol)
