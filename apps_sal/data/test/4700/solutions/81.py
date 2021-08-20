(N, M) = list(map(int, input().split()))
H = list(map(int, input().split()))
peaks = [1] * N
for i in range(M):
    (A, B) = list(map(int, input().split()))
    if H[A - 1] > H[B - 1]:
        peaks[B - 1] = 0
    elif H[B - 1] > H[A - 1]:
        peaks[A - 1] = 0
    else:
        peaks[A - 1] = 0
        peaks[B - 1] = 0
print(sum(peaks))
