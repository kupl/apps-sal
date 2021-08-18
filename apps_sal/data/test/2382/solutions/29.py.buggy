N = int(input())
S = list(map(int, input().split()))
INF = float('inf')

S.sort()

parents = [S[-1]]
S[-1] = INF
checked = 1

for _ in range(N):
    checking = checked
    first = True
    parents.sort(reverse=True)
    for i in parents[:]:
        while True:
            if S[-checking] < i and first:
                parents.append(S[-checking])
                S[-checking] = INF
                checked = checking + 1
                break
            elif S[-checking] < i:
                parents.append(S[-checking])
                S[-checking] = INF
                break
            else:
                checking += 1
                first = False
            if checking == 2 ** N + 1:
                print('No')
                return
else:
    print('Yes')
