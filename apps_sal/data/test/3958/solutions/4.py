def read_data():
    a = list(map(int, list(input().strip())))
    return a

def solve():
    sol = []
    pos = -1
    try:
        for i in range(0,len(a)):
            if a[i] == 0:
                if pos > -1:
                    sol[pos].append(i+1)
                    pos -= 1
                else:
                    sol.append([i+1])
            else:
                pos += 1
                sol[pos].append(i+1)
    except:
        return -1
    if pos == -1:
        return sol
    else:
        return -1

def print_sol(sol):
    if sol == -1:
        print(sol)
        return 0
    print(len(sol))
    for list in sol:
        print(len(list), *list)

a = read_data()
sol = solve()
print_sol(sol)

