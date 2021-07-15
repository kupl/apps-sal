A,B,C= map(int, input().split())

kei = A*C

if B >= kei:
    print(C)
else:
    print(int(B/A))
