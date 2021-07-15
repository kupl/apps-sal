n = int(input())
a = input().strip()
cnt = 0
a = list(a)
for i in range(n):
    if a[i] == 'x':
        cnt += 1
res = abs(n // 2 - max(cnt, n - cnt))
print(res)
if cnt > n - cnt:
    for i in range(n):
        if a[i] == 'x' and res:
            a[i] = 'X'
            res -= 1
else:
    for i in range(n):
        if a[i] == 'X' and res:
            a[i] = 'x'
            res -= 1    
print(''.join(a))        
