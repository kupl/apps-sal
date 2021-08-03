r, c = map(int, input().split())
a = [input() for i in range(r)]
n = len([0 for s in a if 'S' not in s])
m = len([0 for j in range(c) if len([s[j] for s in a if s[j] == '.']) == r])
print(n * c + m * r - n * m)
