import sys
import collections

N, *A = map(int, open(0).read().split())

B = collections.Counter(A).most_common()
B.sort(key=lambda x: x[0])

ans = 0
for i in range(len(B)):
    count = B[i][1]
    if i + 1 < len(B) and B[i + 1][0] == B[i][0] + 1:
        count += B[i + 1][1]
        if i + 2 < len(B) and B[i + 2][0] == B[i][0] + 2:
            count += B[i + 2][1]
    ans = max(ans, count)
print(ans)
