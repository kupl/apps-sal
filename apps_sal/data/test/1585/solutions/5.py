X, Y = map(int, input().split())
CNT = 0
while X*2**CNT <= Y:
    CNT += 1
print(CNT)
