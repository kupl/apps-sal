(A, B, C, D) = map(int, input().split())
s1 = A * B
s2 = C * D
if s1 == s2:
    print(s1)
elif s1 > s2:
    print(s1)
else:
    print(s2)
