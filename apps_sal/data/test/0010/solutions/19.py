def solve(n):
    res = (n // 7) * 2
    d = n % 7
    if (d == 6):
        minn = res + 1
        maxx = res + 2
    elif (d == 1):
        minn = res
        maxx = res + 1
    elif (d == 0):
        minn = res
        maxx = res
    else:
        minn = res
        maxx = res + 2
    return [minn, maxx]


n = int(input())
sol = solve(n)
print(str(sol[0]) + " " + str(sol[1]))
