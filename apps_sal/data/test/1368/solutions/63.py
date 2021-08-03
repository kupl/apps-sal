from collections import Counter
from math import factorial

N, A, B = list(map(int, input().split()))
V = list(map(int, input().split()))

V.sort(reverse=True)
c = Counter(V)

ans = []
L = []
for i in range(A, B + 1):

    ans.append(sum(V[0:i]) / i)
max_ans = max(ans)
print(('{:.6f}'.format(max_ans)))

num = 0
for j in range(B - A + 1):
    tmp = 1
    if ans[j] == max_ans:
        k = V[:A + j]
        cnt_k = Counter(k)
        for key, value in list(cnt_k.items()):
            tmp *= factorial(c[key]
                             ) // factorial(value) // factorial(c[key] - value)
        num += tmp

print(num)
