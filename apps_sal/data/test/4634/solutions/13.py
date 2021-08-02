rn = lambda: int(input())
rl = lambda: list(map(int, input().split()))
rns = lambda: map(int, input().split())
rs = lambda: input()
yn = lambda x: print('Yes') if x else print('No')
YN = lambda x: print('YES') if x else print('NO')

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
