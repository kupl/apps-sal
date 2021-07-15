A,B,C,D = map(int, input().split())

if (C<A and D<=A) or (B<=C and C<D):
    time = 0
else:
    if A<=C and D<=B:
        time = D-C
    elif C<=A and B<=D:
        time = B-A
    elif C<=A and D<=B:
        time = D-A
    elif A<=C and B<=D:
        time = B-C
print(time)
