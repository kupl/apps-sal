a = input().split()[0]
b = ''

for i in range(len(a)):
    if(i % 2 == 0):
        b += a[i]

print(b)
