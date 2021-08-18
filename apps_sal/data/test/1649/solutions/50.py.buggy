abcd = list(map(int, input().split()))
k = 4

for i in range(2 ** k):
    tmp = 0
    for j in range(k):
        if ((i >> j) & 1):
            tmp += abcd[j]
    if tmp == sum(abcd) - tmp:
        print('Yes')
        return
print('No')
