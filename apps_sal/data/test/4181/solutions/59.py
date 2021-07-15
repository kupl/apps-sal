N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

cnt = 0
for i in range(0,N):
    #隣の町で余った勇者を現在の町へ増援
    #更に隣の町へは増援できないことに注意
    if B[i] <= A[i]:
        cnt += B[i]
    elif B[i] > A[i] and B[i] <= A[i]+A[i+1]:
        cnt += B[i]
        A[i+1] = A[i+1] -B[i] + A[i]
    else:
        cnt += A[i]+A[i+1]
        A[i+1] = 0
        
print(cnt)

