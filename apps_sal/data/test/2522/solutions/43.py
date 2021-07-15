import bisect, heapq
N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

for i in range(1,N+1):
    a = bisect.bisect_right(A,i) - bisect.bisect_left(A,i)
    b = bisect.bisect_right(B,i) - bisect.bisect_left(B,i)

    if a + b > N:
        print("No")
        return

B = B[::-1]

j, bef = 0, -1
for i in range(N):
    if A[i] != bef:
        j = 0
    if A[i] == B[i]:
        while j < N:
            if A[j] != B[i] and B[j] != A[i]:
                B[i], B[j] = B[j], B[i]
                break
            j += 1
    bef = A[i]

print("Yes")
for b in B:
    print(b,end=" ")
print("")
