N = int(input())
P = list(map(int, input().split()))
c = 10 ** 20
con = 0
for i in range(N):
    if c > P[i]:
        con += 1
        c = P[i]
print(con)
