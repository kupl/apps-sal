(n, m) = map(int, input().split())
s = {input() for i in range(n)}
print('No' if any((sum((si[j] == '#' for si in s)) > 1 for j in range(m))) else 'Yes')
