(n, m) = map(int, input().strip().split())
for i in range(m):
    (r, s) = map(int, input().strip().split())
s = ''
for i in range(n):
    if i % 2 == 0:
        s = s + '0'
    else:
        s = s + '1'
print(s)
