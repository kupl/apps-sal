n = int(input())
ai = list(map(int,input().split()))
num = 2 * 10 ** 5 + 1
sums = [0] * num
for i in range(n):
    for j in range(i+1,n):
        sums[ai[i] + ai[j]] += 1
print(max(sums))

