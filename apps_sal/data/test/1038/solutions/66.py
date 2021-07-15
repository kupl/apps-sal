import math

A, B = map(int, input().split())

a_p = math.ceil(A/4)
b_p = math.floor(B/4)

ans = 0

for i in range(A, 4*a_p):
    ans = ans ^ i
for j in range(b_p*4, B+1):
    ans = ans ^ j
print(ans)
