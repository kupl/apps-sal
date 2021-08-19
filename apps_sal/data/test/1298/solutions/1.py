n = int(input())
s = input()
z = 0
o = 0
for i in s:
    if i == '0':
        z += 1
    else:
        o += 1
print(abs(z - o))
