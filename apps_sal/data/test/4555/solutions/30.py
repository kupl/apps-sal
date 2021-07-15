#B - Small and Large Integers
A,B,K = map(int,input().split())

ans = []
for j in range(K):
    a = A+j
    b = B-j
    if a > B or b < A:
        break
    ans.append(a)
    ans.append(b)

ans = list(sorted(set(ans), reverse = False))

for i in ans:
    print(i)
