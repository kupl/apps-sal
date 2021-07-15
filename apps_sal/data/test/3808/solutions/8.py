def solvea():
    n = int(input())
    d = int(input())
    e = 5 * int(input())
    best = 0
    for enr in range(n // e + 1):
        curr = e * enr
        curr += d * ((n - curr) // d)
        if curr <= n and curr > best:
            best = curr
    print(n - best)


def solveb():
    a = int(input())
    b = int(input())
    n = int(input())
    ans = 0
    for i in range(a + 1):
        for j in range(b + 1):
            if i + j == n:
                ans += 1
    print(ans)


def solvec():
    n = int(input())
    curr_bal = 0
    min_bal = 0
    for e in input():
        if e == '(':
            curr_bal += 1
        else:
            curr_bal -= 1
        if curr_bal < min_bal:
            min_bal = curr_bal
    if min_bal >= -1 and curr_bal == 0:
        print('Yes')
    else:
        print('No')


def __starting_point():
    solvec()

__starting_point()
