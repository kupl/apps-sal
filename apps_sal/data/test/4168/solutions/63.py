import sys
 
N = int(sys.stdin.readline())
if N == 0:
    print(0)
    return
binN = ""
pN = abs(N)
while N != 0:
    if abs(N % -2) == 1:
        binN += "1"
    else:
        binN += "0"
    N += N%(-2)
    N //= -2
print(binN[::-1])
