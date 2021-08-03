def rn(): return int(input())
def rl(): return list(map(int, input().split()))
def rns(): return map(int, input().split())
def rs(): return input()
def yn(x): return print('Yes') if x else print('No')
def YN(x): return print('YES') if x else print('NO')


for _ in range(rn()):
    x = rs()
    n = int(x[0])
    ans = 10 * (n - 1)
    for i in range(len(x) + 1):
        ans += i
    print(ans)
