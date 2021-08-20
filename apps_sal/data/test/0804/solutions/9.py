a = input()
k = int(input())
A = {}
for i in a:
    A[i] = 1
if len(a) < k:
    print('impossible')
elif k - len(A) > 0:
    print(k - len(A))
else:
    print(0)
