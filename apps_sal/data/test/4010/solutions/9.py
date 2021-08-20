t = int(input())
for i in range(t):
    n = int(input())
    data = tuple(map(int, input().split()))
    met = []
    for i in data:
        if i in met[:-1]:
            print('YES')
            break
        met.append(i)
    else:
        print('NO')
