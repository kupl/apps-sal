p, k = input().strip().split(' ')
flag = 1
p = int(p)
k = int(k)
A = []
B = []
k = -k
while p != 0:
    A.append(p % k)
    p //= k
    if A[-1] < 0:
        p += 1
for i in A:
    if i < 0:
        B.append(i - k)
    else:
        B.append(i)
print(len(B))
for i in B:
    print(i, end=" ")
