def read(type = 1):
    if type:
        file = open("input.dat", "r")
        n = int(file.readline())
        a = []
        for i in range(n):
            a.append(list(map(int, file.readline().split())))
        file.close()
    else:
        n = int(input().strip())
        a = []
        for i in range(n):
            a.append(list(map(int, input().strip().split())))
    return n, a


def solve():
    sol = [1]
    used = [0 for i in range(n)]
    while len(sol) < n - 1:
        last = sol[-1] - 1
        used[last] = 1
        if a[last][0] in a[a[last][1]-1]:
            sol.append(a[last][1])
            used[a[last][1]-1] = 1
            sol.append(a[last][0])
        else:
            sol.append(a[last][0])
            used[a[last][0] - 1] = 1
            sol.append(a[last][1])
    used[sol[-1] - 1] = 1
    if len(sol) != n:
        for i in range(n):
            if used[i] == 0:
                sol.append(i+1)
    return sol


def write(sol):
    line = ""
    for v in sol:
        line += str(v) + " "
    print(line)


n, a = read(0)
sol = solve()
write(sol)
