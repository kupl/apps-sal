import math
n, k = map(int, input().split())

tmp = 0
cumsum = [0]
for i in map(int, input().split()):
    tmp += i
    cumsum.append(tmp)
total = 0
for end in range(n):
    if cumsum[end + 1] - cumsum[0] >= k:
        tmpstart = 0
        tmpend = end
        tmp = (tmpstart + tmpend) // 2
        while tmpstart != tmpend:
            if (cumsum[end + 1] - cumsum[tmp] >= k) and (cumsum[end + 1] - cumsum[tmp + 1] >= k):
                tmpstart = tmp + 1
            elif (cumsum[end + 1] - cumsum[tmp] < k) and (cumsum[end + 1] - cumsum[tmp + 1] < k):
                tmpend = tmp - 1
            else:
                tmpstart = tmp
                tmpend = tmp
            tmp = (tmpstart + tmpend) // 2
        total += tmp + 1

print(total)
