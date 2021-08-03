def rn(): return int(input())
def rl(): return list(map(int, input().split()))
def rns(): return map(int, input().split())
def rs(): return input()
def yn(x): return print('Yes') if x else print('No')
def YN(x): return print('YES') if x else print('NO')


for _ in range(rn()):
    n = rn()
    l = rl()
    ans = 0
    start = False
    acc = 0
    for i in l:
        if i == 1:
            start = True
            ans += acc
            acc = 0
        elif start:
            acc += 1
    print(ans)
