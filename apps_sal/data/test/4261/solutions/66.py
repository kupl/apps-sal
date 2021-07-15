A,B,C= map(int, input().split())

space1 = A-B
if space1 > C:
    print(0)
else:
    print(C-space1)
