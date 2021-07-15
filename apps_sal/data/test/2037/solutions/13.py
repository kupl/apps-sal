n, m = map(int, input().split())
mas = list(map(int, input().split()))
pol = [0] * n
null = 0
ans = ''
for i in range(m):
    pol[mas[i] - 1] += 1
    if pol[mas[i] - 1] == 1:
        null += 1
    if null == n:
        ans += '1'
        null = 0
        for j in range(n):
            pol[j] -= 1
            if pol[j] != 0:
                null += 1
    else:
        ans += '0'
print(ans)        
