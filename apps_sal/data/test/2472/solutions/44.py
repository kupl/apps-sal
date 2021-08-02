from operator import itemgetter
n = int(input())
ab = [list(map(int, input().split())) for i in range(n)]
ab = sorted(ab, key=itemgetter(1))
for i in range(n):
    if ab[i][0] > ab[i][1]:
        print("No")
        return
    if i != n - 1:
        ab[i + 1][0] += ab[i][0]
    else:
        print("Yes")
