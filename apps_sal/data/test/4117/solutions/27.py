# 入力
N = int(input())
L = list(map(int, input().split()))

# 処理
L.sort()
count = 0
for i in range(N):
    for j in range(0, i):
        for k in range(0, j):
            if (L[i] != L[j] != L[k]
                    and L[k] + L[j]  > L[i]):
                count += 1

print(count)
