N = int(input())
A = list(map(int, input().split()))
count = 0
mh = A[0]
for i in range(1, len(A)):
    if mh > A[i]:
        count += mh - A[i]
    else:
        mh = A[i]
print(count)
