n =  int(input())
A = []
for i in range(n):
    A.append(int(input()))
ma = max(A)
ma2 = sorted(A)[-2]
for a in A:
    if a == ma:
        print(ma2)
    else:
        print(ma)
