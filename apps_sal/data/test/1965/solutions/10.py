import sys
ii = lambda: sys.stdin.readline().strip()
idata = lambda: [int(x) for x in ii().split()]

def solve():
    n, x = idata()
    data = idata()
    flag = 0
    summ = 0
    for i in range(n):
        summ += data[i]
        if data[i] == x:
            flag += 1
    if flag == n:
        print(0)
        return
    if flag:
        print(1)
        return
    if summ // n == x and summ % n == 0:
        print(1)
        return
    print(2)
    return

for t in range(int(ii())):
    solve()

