n = int(input())
a=list(map(int, input().split()))
a.sort()
A = []
B = []
for i in range(1,n+1):
    if i % 2 != 0:
        A.append(a[-i])
    else:
        B.append(a[-i])
print(sum(A) - sum(B))
