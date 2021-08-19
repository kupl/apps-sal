(A, B, C, D) = [int(input()) for i in range(4)]
if A <= B:
    train = A
else:
    train = B
if C <= D:
    bus = C
else:
    bus = D
answer = train + bus
print(answer)
