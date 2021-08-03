n = input()

s = 0
for i in range(len(n)):
    s += int(n[i])

print('Yes') if int(n) % s == 0 else print('No')
