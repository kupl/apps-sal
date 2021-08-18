N, M = map(int, input().split())
Hlist = list(map(int, input().split()))
ABlist = []
for _ in range(M):
    ABlist.append(list(map(int, input().split())))
flaglist = [1] * N
for row in ABlist:
    one = row[0] - 1
    two = row[1] - 1
    if Hlist[one] <= Hlist[two]:
        flaglist[one] = 0
    if Hlist[one] >= Hlist[two]:
        flaglist[two] = 0
print(sum(flaglist))
