import bisect
N = int(input())
X = list(map(int, input().split()))
X_sorted = sorted(X)
pre_med_index = N // 2 - 1
pos_med_index = N // 2
for i in range(N):
    if X[i] <= X_sorted[pre_med_index]:
        print(X_sorted[pos_med_index])
    else:
        print(X_sorted[pre_med_index])
