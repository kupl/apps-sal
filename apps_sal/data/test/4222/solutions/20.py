[N, K] = [int(i) for i in input().split()]
okasi = [0] * N
for k in range(K):
    num = int(input())
    have = [int(i) for i in input().split()]
    for snuke in have:
        okasi[snuke - 1] = num
print(okasi.count(0))
