from math import ceil

n = int(input())
a = int(input())
b = int(input())
#5
k = 2 * b + 4 * a
br = 0

if 2 * b <= n and b < a and a + b > n:
    br = 5
    
elif 2 * a > n and 2 * b > n and a + b > n:
    br = 6
   
elif k <= n:
    br = 1

elif b + 2 * a <= n:
    br = 2

elif a + b <= n and 2 * a <= n or 4 * a <= n:
    br = 3

else:
    br = 4


print(br)


