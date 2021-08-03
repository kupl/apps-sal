n, k, q = [int(i) for i in input().split()]
dic = {}
for i in range(n):
    dic[i] = k
for _ in range(q):
    dic[int(input()) - 1] += 1
for i in range(n):
    if dic[i] - q > 0:
        print('Yes')
    else:
        print('No')
