n = int(input())
al = list(map(int, input().split()))

res = 0
temp = 0
for i in range(n):
    if al[i] >= temp:
        res += al[i] - temp
        temp = al[i]
    else:
        temp = al[i]

print(res)
