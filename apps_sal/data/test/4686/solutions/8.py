w = input()

a = ord('a')
z = ord('z')

for i in range(a,z+1):
    x = w.count(chr(i))
    if x%2 == 1:
        print('No')
        return
    
print('Yes')

