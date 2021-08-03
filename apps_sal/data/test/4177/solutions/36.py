s = input()
l = list(s)

for i in range(len(l)):
    l[i] = 'x'

s = ''.join(l)

print(s)
