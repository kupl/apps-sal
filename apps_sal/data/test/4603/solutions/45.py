A = int(input())
B = int(input())
C = int(input())
D = int(input())

if A <= B:
    train = A
else:
    train = B
if C <= D:
    bus = C
else:
    bus = D

answer = (train + bus)
print(answer)
