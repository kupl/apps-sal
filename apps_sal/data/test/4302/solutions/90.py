A, B = map(int, input().split())
s = 0
for i in range(2):
    if A > B:
        s += A
        A -= 1
    elif B > A:
        s += B
        B -= 1
    elif A == B:
        s += A
        A -= 1
print(s)
