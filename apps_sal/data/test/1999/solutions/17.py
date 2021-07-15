def read_data():
    n = int(input().strip())
    a = list(map(int, list(input().strip().split())))
    return n, a

def solve():
    s = {}
    for i in range(len(a)):
        j = a[i]
        while j in s:
            del s[j]
            j *= 2
        s[j] = i

    sol = list(sorted(s.keys(), key=lambda j: s[j]))
    print(len(sol))
    print(*sol)

n, a = read_data()
solve()
