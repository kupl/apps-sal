import sys
N = int(input())
if N == 2:
    print(2)
    return
n = N - 1
Flag = True
while Flag:
    n += 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            break
        if i == int(n**0.5) and n % i != 0:
            Flag = False

print(n)
