n = int(input())
mass = ['W', 'B']
s = ''
for i in range(n + 2):
    s += mass[i % 2]
for i in range(n):
    print(s[i % 2:n + i % 2])
