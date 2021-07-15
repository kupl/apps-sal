n, k = map(int, input().split())
al = [0]*(10**5+1)

for _ in range(n):
    a, b = map(int, input().split())
    al[a] += b

cnt = 0
i = 0
while cnt < k:
    cnt += al[i]
    i += 1

print(i-1)
