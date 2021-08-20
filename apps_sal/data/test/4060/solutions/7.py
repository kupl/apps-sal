def read(type=1):
    if type:
        file = open('input.dat', 'r')
        n = int(file.readline())
        a = file.readline()
        file.close()
    else:
        n = int(input().strip())
        a = input().strip()
    return (n, a)


def solve():
    sol = 0
    vs = []
    v = 0
    for i in range(n):
        if a[i] == '(':
            v += 1
        else:
            v -= 1
        vs.append(v)
    mins = [10000000 for i in range(n)]
    last = n
    for i in range(n):
        if i:
            mins[n - i - 1] = min(vs[n - i - 1], mins[n - i])
        else:
            mins[n - i - 1] = vs[n - i - 1]
        if vs[n - i - 1] < 0:
            last = n - i - 1
    for i in range(n):
        if a[i] == '(' and vs[n - 1] == 2:
            if i:
                if mins[i] >= 2:
                    sol += 1
        if a[i] == ')' and vs[n - 1] == -2:
            if i != n - 1:
                if mins[i] >= -2:
                    sol += 1
        if i == last:
            break
    return sol


(n, a) = read(0)
sol = solve()
print(sol)
