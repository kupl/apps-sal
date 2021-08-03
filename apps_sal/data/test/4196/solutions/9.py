import math

N = int(input().rstrip())
A = list(map(int, input().rstrip().split()))
l = [A[0]]
r = [A[-1]]
for i in range(len(A) - 1):
    l.append(math.gcd(A[i + 1], l[i]))
    r.append(math.gcd(A[-(i + 2)], r[i]))
ans = []
ans.append(r[-2])
for i in range(len(A) - 2):
    ans.append(math.gcd(l[i], r[-(i + 3)]))
ans.append(l[-2])
print(max(*ans))
