n = int(input())

a = n % 1000
if(a == 0):
    a = 0

else:
    a = 1000 - a

print(a)
