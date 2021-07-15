N = int(input())
 
s = input()

ones = 0
zeros = 0

for letter in s:
    if letter=='1':
        ones += 1
    else:
        zeros += 1
        
if ones!=zeros:
    print(1)
    print(s)
else:
    print(2)
    print(s[0],s[1:],sep=' ')
