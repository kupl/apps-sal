A,B=map(int,input().split())
if A>=13:
    print(B)
elif A>=6 and A<=12:
    print(int(B/2))
else:
    print(0)
