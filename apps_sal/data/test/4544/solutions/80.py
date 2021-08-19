import collections
n = int(input())
a = list(map(int, input().split()))

lis = collections.Counter(a)
ans = 0
memo = 0
# print(lis)

for i in range(10**5):
    memo = lis[i - 1] + lis[i] + lis[i + 1]
    #print(lis[i-1], lis[i], lis[i+1])
    if memo > ans:
        ans = memo


print(ans)
