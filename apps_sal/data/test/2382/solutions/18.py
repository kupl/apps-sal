N = int(input())
M = 2**N
A = list(map(int,input().split()))
A.sort(reverse=True)

ar = [A[0]]
A[0] = -1
for _ in range(N):
    ar.sort(reverse=True)
    br = []
    i = 0
    while i < M and len(br) < len(ar):
        if A[i] >= 0:
            if ar[len(br)] > A[i]:
                br.append(A[i])
                A[i] = -1
        i += 1
    if len(br) < len(ar):
        print('No')
        return
    ar += br
print('Yes')
