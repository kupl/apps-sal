N = int(input())
A = []
for i in range(N):
    a = int(input())
    A.append(a)
B = sorted(A)
if B[-1] != B[-2]:
    t = A.index(B[-1])
    for i in range(N):
        if i == t:
            print(B[-2])
        else:
            print(B[-1])
else:
    for i in range(N):
        print(B[-1])
