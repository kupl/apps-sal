A, B, C, D = map(int, input().split())

LWeight = A + B
RWeight = C + D

if LWeight > RWeight:
    print("Left")
elif LWeight < RWeight:
    print("Right")
else:
    print("Balanced")
