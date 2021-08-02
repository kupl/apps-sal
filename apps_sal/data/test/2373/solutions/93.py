N = int(input())
ls = list(map(int, input().split()))
ii = 0
for i in range(N - 1):
    if i + 1 == ls[i]:
        ii += 1
        ls[i + 1] = 0
if N == ls[N - 1]:
    ii += 1
print(ii)
