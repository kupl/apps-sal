a = list(map(int,input().split()))

N = a[0]
M = a[1]

ctr = [0 for i in range(M)]


for i in range(N):
    b =  list(map(int,input().split()))

    for j in range(b[0]):
        for k in range(M):
            if b[j+1] == k+1:
                ctr[k] += 1

flag = [N == ctr[j] for j in range(M)]
print(sum(flag))
