N, K = (int(x) for x in input().split())
listN = [1] * N
for i in range(K):
    d = int(input())
    tmp = list(map(int, input().split()))
    for j in tmp:
        listN[j - 1] = 0
print((sum(listN)))
