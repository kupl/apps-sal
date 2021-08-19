(n, m) = map(int, input().split())
for i in range(m):
    s = input()
ans = []
for i in range(n):
    if i % 2 == 0:
        ans.append('0')
    else:
        ans.append('1')
print(''.join(ans))
