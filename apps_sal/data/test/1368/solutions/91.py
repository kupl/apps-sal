import math
def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
N,A,B= (int(x) for x in input().split())
v = list(map(int, input().strip().split()))
v.sort(reverse=True)
print((sum(v[0:A])/A))
ctall = 0
ct = 0
for i in range (A):
    if v[i] == v[A-1]:
        ct += 1
answer = 0
for i in range (N):
    if v[i] == v[A-1]:
        ctall += 1
    if v[i] < v[A-1]:
        break
if (ct == A):
    for i in range(A,min(ctall+1,B+1)):
        answer += combinations_count(ctall, i)
    print(answer)
else: print((combinations_count(ctall, ct)))

