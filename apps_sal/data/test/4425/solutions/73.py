import math
answer = 0
n, k = map(int, input().split())
for i in range(1, n + 1):
    if(i >= k):
        answer += 1 / n
    else:
        answer += 1 / (2**math.ceil(math.log2(k / i))) / n
print(answer)
