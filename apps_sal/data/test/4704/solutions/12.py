n = int(input())
L = list(map(int, input().split()))

li = [0]

for i in range(n):
    li.append(li[i] + L[i])

sumL = sum(L)
# print(sumL)
ans = 10**10
for i in range(1, n):
    diff = abs(li[i] - (sumL - li[i]))
    # print(diff,li[i],sumL-li[i])
    ans = min(ans, diff)
print(ans)
