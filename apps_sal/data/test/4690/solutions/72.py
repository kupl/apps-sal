A,B,C,D = map(int,input().split())

ab = A * B
cd = C * D

if ab > cd:
    print(ab)
elif cd > ab:
    print(cd)
else:
    print(ab)
