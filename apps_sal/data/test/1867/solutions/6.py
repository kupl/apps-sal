def cmp_to_key(mycmp):
    'Convert a cmp= function into a key= function'

    class K:
        def __init__(self, obj, *args):
            self.obj = obj

        def __lt__(self, other):
            return mycmp(self.obj, other.obj) < 0

        def __gt__(self, other):
            return mycmp(self.obj, other.obj) > 0

        def __eq__(self, other):
            return mycmp(self.obj, other.obj) == 0

        def __le__(self, other):
            return mycmp(self.obj, other.obj) <= 0

        def __ge__(self, other):
            return mycmp(self.obj, other.obj) >= 0

        def __ne__(self, other):
            return mycmp(self.obj, other.obj) != 0

    return K


def compare(x, y):
    if x[2] != y[2]:
        return y[2] - x[2]
    return (x[1] - x[0]) - (y[1] - y[0])


def main():
    n = int(input())
    d = list(map(int, input().split()))
    r = {}
    for i in range(n):
        if d[i] in r:
            r[d[i]] = [r[d[i]][0], i + 1, r[d[i]][2] + 1]
        else:
            r[d[i]] = [i + 1, i + 1, 1]

    sr = sorted(list(r.values()), key=cmp_to_key(compare))
    print(sr[0][0], sr[0][1])


main()
