# Nを取得する
N = int(input())

# リストのLを取得する
L = list(map(int, input().split()))

# Lの三つの組み合わせ全部に対して条件を検証する
counter=0
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            # Li, Lj, Lkの全ての値が異なり、三角形の条件を満たすならcounter+1
            if len(set([L[i], L[j], L[k]])) == 3 and L[i]+L[j]>L[k] and L[j]+L[k]>L[i] and L[k]+L[i]>L[j]:
                counter += 1
                
print(counter)
