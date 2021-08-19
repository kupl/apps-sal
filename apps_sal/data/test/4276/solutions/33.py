(n, T) = map(int, input().split())
ct = [list(map(int, input().split())) for _ in range(n)]
li = []
for k in ct:
    if k[1] <= T:
        li += [k[0]]
if li == []:
    print('TLE')
else:
    print(min(li))
