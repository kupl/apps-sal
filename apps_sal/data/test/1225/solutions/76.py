H = int(input())
b = 0
while 2**b <= H:
    b += 1
print((2**(b) - 1))
