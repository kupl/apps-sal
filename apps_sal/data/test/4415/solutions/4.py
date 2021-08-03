n = int(input())
A = list(map(int, input().split()))

B = set()
C = set()
yes = True

for i in A:
    if i not in B:
        B.add(i)
    elif i not in C:
        C.add(i)
    else:
        print('NO')
        yes = False
        break

if yes:
    print('YES')

    print(len(B))
    print(*sorted(list(B)))

    print(len(C))
    print(*sorted(list(C), reverse=True))
