n = input()
c = 0
for i in n:
    c += int(i)
print('Yes' if int(n) % c == 0 else 'No')
