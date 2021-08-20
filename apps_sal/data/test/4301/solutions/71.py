N = int(input())
A = [int(input()) for _ in range(N)]
li = A.copy()
li.sort()
f = li[-1]
s = li[-2]
for i in range(N):
    if f == A[i]:
        print(s)
    else:
        print(f)
