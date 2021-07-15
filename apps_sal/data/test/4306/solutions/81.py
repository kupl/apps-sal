A,B,C,D=map(int,input().split())
if B<C or D<A:
    print(0)
elif D>=B and A>=C:
    print(B-A)
elif D>B:
    print(B-C)
elif B>=D and C>=A:
    print(D-C)
else:
    print(D-A)
