import sys
import math
(n, k) = list(map(int, input().split()))
s = list(input())
word = set(input().split())
lenArr = []
sum = 0
for i in range(len(s)):
    if s[i] not in word:
        if sum != 0:
            lenArr.append(sum)
            sum = 0
    else:
        sum += 1
if sum != 0:
    lenArr.append(sum)
    sum = 0
ans = 0
for i in range(len(lenArr)):
    ans += lenArr[i] * (lenArr[i] + 1) // 2
print(ans)
