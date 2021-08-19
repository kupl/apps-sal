(m, n) = list(map(int, input().split()))
t = [set([i for i in list(map(int, input().split()))[1:]]) for _ in range(m)]
for i in range(m - 1):
    for j in range(i + 1, m):
        if len(t[i] & t[j]) == 0:
            print('impossible')
            break
    else:
        continue
    break
else:
    print('possible')
