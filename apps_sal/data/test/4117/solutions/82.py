# Nを取得する
N = int(input())

# L1〜LNをリストとして取得する
L = list(map(int, input().split()))

# Lの3つの値の組み合わせ全てに対して、三角形の条件を検証する
counter = 0
for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            # Li, Lj, Lkの値が全て異なることなり、三角形の条件を満たすならカウント＋１
            if len(set([L[i], L[j], L[k]])) == 3 and L[i] + L[j] > L[k] and L[j] + L[k] > L[i] and L[i] + L[k] > L[j]:
                counter += 1

# 結果を表示
print(counter)
