
n, m = map(int, input().split())

s = input()

for i in range(m):
    a, b, c, d = input().split()
    s = s[:int(a) - 1] + s[int(a) - 1:int(b)].replace(c, d) + s[int(b):]

print(s)
