(n, k) = [int(i) for i in input().split()]
dic = [0] * (k + 1)
for j in range(n):
    a = int(input())
    dic[a] += 1
sets = 0
for d in dic:
    sets += d // 2
tot = (n + 1) // 2
print(sets + tot)
