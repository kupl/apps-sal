(n, m) = list(map(int, input().split()))
a = list(map(int, input().split()))
rec = [0] * n
dic = {}
for i in range(m):
    rec[a[i] - 1] += 1
    dic[rec[a[i] - 1]] = i
t = ['0'] * m
mi = min(rec)
for i in range(1, mi + 1):
    t[dic[i]] = '1'
print(''.join(map(str, t)))
