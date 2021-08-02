def read(type=1):
    if type:
        file = open("input.dat", "r")
        line = list(map(int, file.readline().split()))
        n = line[0]
        m = line[1]
        a = []
        for i in range(m):
            line = tuple(map(int, file.readline().split()))
            if line[0] < line[1]:
                a.append(line)
            else:
                a.append([line[1], line[0]])
        file.close()
    else:
        line = list(map(int, input().strip().split()))
        n = line[0]
        m = line[1]
        a = []
        for i in range(m):
            line = tuple(map(int, input().strip().split()))
            if line[0] < line[1]:
                a.append(line)
            else:
                a.append([line[1], line[0]])

    return n, m, a


def write(sol, x):
    print("YES")
    print(" ".join(map(str, sol[1:-1])))
    sol[x[1]] = sol[x[0]]
    print(" ".join(map(str, sol[1:-1])))


def solve(a):
    if len(a) == n * (n - 1) // 2:
        print("NO")
        return 0
    a = sorted(a, key=lambda x: (x[0], x[1]))
    x = [1, 2]
    for t in a:
        if list(t) != x:
            break
        if x[1] == n:
            x[0] += 1
            x[1] = x[0] + 1
        else:
            x[1] += 1
    sol = [0 for i in range(n + 2)]
    sol[x[0]] = 1
    sol[x[1]] = 2
    v = 3
    for i in range(1, n + 1):
        if i not in x:
            sol[i] = v
            v += 1
    write(sol, x)


n, m, a = read(0)
solve(a)
