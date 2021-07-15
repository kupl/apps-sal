A, op, B = input().split()
A, B = int(A), int(B)

if op == "+":
    ans = A + B
else:
    ans = A - B

print(ans)
