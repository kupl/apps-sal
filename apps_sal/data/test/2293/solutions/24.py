m, n = list(map(int, input().split()))
t = [set([int(i) for i in input().split()][1:]) for j in range(m)]
for i in range(m - 1):
    for j in range(1, m):
        if not (t[i] & t[j]):
            print('impossible')
            return
print('possible')

