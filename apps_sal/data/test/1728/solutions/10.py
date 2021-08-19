n = int(input())
p = list(map(int, input().split()))
c = list(map(int, input().split()))
nbr = 1
for i in range(1, n):
    if c[i] != c[p[i - 1] - 1]:
        nbr += 1
print(nbr)
