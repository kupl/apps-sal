def read(type=1):
    if type:
        file = open('input.dat', 'r')
        line = int(file.readline())
        file.close()
    else:
        line = list(map(int, input().strip().split()))
        n = line[0]
        x = line[1]
        y = line[2]
        line = list(map(int, input().strip().split()))
    return (n, x, y, sorted(line, reverse=True))


def solve():
    sol = 0
    for i in range(len(a)):
        if a[len(a) - 1 - i] + y > x:
            pos = len(a) - 1 - i
            pos = len(a) - 1 - i
            break
    for i in range(len(a)):
        if a[i] <= x:
            sol += 1
            a[pos] += y
            pos -= 1
    if x > y:
        return n
    else:
        return sol


(n, x, y, a) = read(0)
sol = solve()
print(sol)
