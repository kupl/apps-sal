N = int(input())
ls = []
for i in range(N):
    ls.append(tuple(map(int, input().split())))
ls.sort(key=lambda x: x[1]-x[0])
sum = 0
for i in range(N):
    sum+=ls[i][0]*i+ls[i][1]*(N-1-i)
print(sum)

