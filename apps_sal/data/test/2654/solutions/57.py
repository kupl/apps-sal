from operator import itemgetter

n = int(input())
AB = [list(map(int, input().split())) for _ in range(n)]

sortA = sorted(AB, key=itemgetter(0))
sortB = sorted(AB, key=itemgetter(1))

if n%2==1:
    print(sortB[n//2][1] - sortA[-n//2][0] + 1)

else:
    print(int(((sortB[n//2][1]+sortB[n//2-1][1])/2 - (sortA[n//2][0]+sortA[n//2-1][0])/2) / (1/2) + 1))
