A,B = map(int,input().split())
if abs(A-B) >= 1:
    print(max(A,B)*2-1)
else:
    print(2*A)
