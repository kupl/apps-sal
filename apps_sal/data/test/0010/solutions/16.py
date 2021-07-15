import sys
#sys.stdin = open("apples.in","r")
#sys.stdout = open("apples.out","w")

n = int(input())
k = n // 7 
if (n % 7 == 0):
    print(k*2, end = ' ')
elif (n % 7 == 6):
    print(max(k*2+1, 0), end = ' ')
else:
    print(max(k*2, 0), end = ' ')


if (n % 7 == 0):
    print(k*2)
elif (n % 7 == 1):
    print(k*2+1)
else:
    print(k*2+2)

        
#sys.stdin.close()
#sys.stdout.close()

