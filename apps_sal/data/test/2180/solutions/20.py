n = int(input())
c = ['.', 'C']
print((n**2+1)//2)
for i in range(n):
    if i % 2 != 0:
        print(''.join(c[x%2] for x in range(n)))
    else:
        print(''.join(c[x%2-1] for x in range(n)))

