# tsundoku
import bisect
n, m, k = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))

readtime_a = [0]
readtime_b = [0]
for i in range(n):
    readtime_a.append(readtime_a[i] + a[i])
for i in range(m):
    readtime_b.append(readtime_b[i] + b[i])

# print(readtime_a)
# print(readtime_b)

cnt = [0]

for i in range(n + 1):
    if readtime_a[i] > k:
        continue
    else:
        # print(i,bisect.bisect(readtime_b,k-readtime_a[i])-1,k-readtime_a[i])

        cnt.append(i - 1 + bisect.bisect(readtime_b, k - readtime_a[i]))

print((max(cnt)))
