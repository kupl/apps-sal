n = int(input())
for i in range(101):
    if (n-i*7)%4 == 0 and n >= i*7:
        print('Yes')
        return
print('No')
