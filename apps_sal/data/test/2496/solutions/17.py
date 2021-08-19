N = int(input())
A = list(map(int, input().split()))
maxA = max(A)
count = [0] * (maxA + 1)
for x in A:
    count[x] += 1
maxc = 0
for i in range(2, maxA + 1):
    maxc = max(maxc, sum(count[i::i]))
if maxc == N:
    print('not coprime')
elif maxc <= 1:
    print('pairwise coprime')
else:
    print('setwise coprime')
