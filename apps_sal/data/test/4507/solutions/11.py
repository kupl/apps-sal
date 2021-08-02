from sys import stdin, stdout

n, m, k = tuple(map(lambda x: int(x), stdin.readline().split()))
a = stdin.readline().split()
for i in range(len(a)):
    a[i] = int(a[i])
prefix_sum = []
a = sorted(a, key=lambda x: x)
for x in a:
    if prefix_sum:
        prefix_sum.append(prefix_sum[-1] + x)
    else:
        prefix_sum.append(x)

offers = {}
for i in range(m):
    x, y = stdin.readline().split()
    x = int(x)
    y = int(y)
    if x not in offers or y > offers[x]:
        offers[x] = y


answer = []
for i in range(k):
    if i == 0:
        if 1 in offers and offers[1] > 0:
            answer.append(0)
        else:
            answer.append(a[0])
        continue
    answer.append(400000002)
    for j in range(i):
        cursum = answer[j]
        answer[i] = min(answer[i], answer[j] + prefix_sum[i] - prefix_sum[j + (offers[i - j] if (i - j) in offers else 0)])
    answer[i] = min(answer[i], prefix_sum[i] if (i + 1) not in offers else (-prefix_sum[offers[i + 1] - 1] + prefix_sum[i]))


print(answer[k - 1])
