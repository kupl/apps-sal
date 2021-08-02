n = int(input())
p = list(map(int, input().split()))
f = 0
for i in range(n):
    s = input()
    if s.count('a') + s.count('e') + s.count('i') + s.count('o') + s.count('u') + s.count('y') == p[i]:
        f += 1
if f == n:
    print('YES')
else:
    print('NO')
