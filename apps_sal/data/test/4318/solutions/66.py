N = int(input())
ls = list(map(int,input().split()))
m = 0
ii = 0
for i in range(N):
    if m <= ls[i]:
        ii += 1
        m = ls[i]
    else:
        continue
print(ii)
