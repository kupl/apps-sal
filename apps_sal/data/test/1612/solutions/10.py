n = int(input())
a = []
for i in range(n):
    a += [set(list(map(int, input().split()))[1:])]
for i in range(n):
    for j in range(n):
        if i != j and a[j] <= a[i]:
            print('NO')
            break
    else:
        print('YES')
