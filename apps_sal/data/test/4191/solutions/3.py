a = int(input())
b = int(input())
c = int(input())
d = int(input())
A = a ^ b
B = c or d
C = b and c
D = a ^ d
AA = A and B
BB = C or D
ans = AA ^ BB
print(ans)
