n = int(input())
l = list(map(int, input().split()))
s = ''
for i in range(n):
    s += str(l[i])
j = 0
while j != n and l[j] == l[0]:
    j += 1
ans = ''
blocks = n // j
curr = l[0]
for i in range(blocks):
    ans += j * str(curr)
    curr ^= 1
if ans == s:
    print('YES')
else:
    print('NO')
