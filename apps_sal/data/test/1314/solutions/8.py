n = int(input())
p = [tuple(map(int, input().split())) for _ in range(n)]
q = [tuple(map(int, input().split())) for _ in range(n)]
(sumx, sumy) = (0, 0)
for (i, j) in p:
    sumx += i
    sumy += j
for (i, j) in q:
    sumx += i
    sumy += j
sumx //= n
sumy //= n
print(sumx, sumy)
