# A - Traveling Budget

A = int(input())
B = int(input())
C = int(input())
D = int(input())

if A <= B:
    if C <= D:
        answer = A + C
    else:
        answer = A + D
elif C <= D:
    answer = B + C
else:
    answer = B + D

print(answer)
