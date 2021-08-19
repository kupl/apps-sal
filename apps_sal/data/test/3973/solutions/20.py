import sys
input = sys.stdin.readline
N, M = map(int, input().split())
a = list(map(int, input().split()))
d = [0] * (N - 1)
imosa = [0] * (M * 2 + 2)
imosb = [0] * (M * 2 + 2)
for i in range(N - 1):
    if a[i + 1] >= a[i]:
        d[i] = a[i + 1] - a[i]
        imosa[a[i] + 1] += 1
        imosa[a[i + 1] + 1] -= 1
        imosb[a[i] + 1] -= a[i] + 1
        imosb[a[i + 1] + 1] += a[i] + 1
    else:
        d[i] = a[i + 1] + M - a[i]
        imosa[a[i] + 1] += 1
        imosa[a[i + 1] + M + 1] -= 1
        imosb[a[i] + 1] -= a[i] + 1
        imosb[a[i + 1] + M + 1] += a[i] + 1
    # print(imosb)
# print(d)

imos = [0] * (M + 2)
for i in range(2 * M + 1):
    imosa[i + 1] += imosa[i]
    imosb[i + 1] += imosb[i]
# print(imosa)
# print(imosb)
for i in range(M + 2):
    imos[i] = imosa[i] * i + imosa[i + M] * (i + M) + imosb[i] + imosb[i + M]
# print(imos)
print(sum(d) - max(imos[1: M + 1]))
