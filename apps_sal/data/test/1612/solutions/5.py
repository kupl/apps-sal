3


def readln():
    return tuple(map(int, input().split()))


(n,) = readln()
lst = [set(readln()[1:]) for _ in range(n)]
for a in lst:
    print('YES' if len([1 for b in lst if len(a.union(b)) == len(a)]) == 1 else 'NO')
