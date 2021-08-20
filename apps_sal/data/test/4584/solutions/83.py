n = int(input())
aa = [0] + list(map(int, input().split()))
buka = [0] * n
for i in range(1, n):
    buka[aa[i] - 1] += 1
for i in range(n):
    print(buka[i])
