import itertools

n, m = list(map(int, input().split()))
lis = []
for i in range(m):
    a, b = list(map(int, input().split()))
    lis.append((a, b))

LIS = [i for i in range(2, n + 1)]
big_lis = list(itertools.permutations(LIS))
L = len(big_lis)

ans2 = 0
for j in range(L):
    i = 1
    ans1 = 1
    for k in big_lis[j]:
        if((i, k) not in lis) & ((k, i) not in lis):
            ans1 = 0
        i = k
    ans2 += ans1
print(ans2)

