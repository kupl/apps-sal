from collections import defaultdict

n, k = list(map(int, input().split()))
A = list(map(int, input().split()))
ans = 0
shukei = defaultdict(int)
# AiからAjまでの和→SA[j]-SA[i-1]
# SA[j]-SA[i-1]=j-(i-1)
# 今回はkで割ったあまりなのでaccumulateは使わず自力
S = [0] * (n + 1)
T = [0] * (n + 1)
for i in range(1, n + 1):
    S[i] = S[i - 1] + A[i - 1]
    S[i] %= k
    T[i] = S[i] - i
    T[i] %= k
# i>=1, i<jで同じ値になっている組み合わせを探せば良い。
# kで割ったあまりなので、要素数j−(i-1)がkより小さくないといけない
ans = 0
if k > n + 1:
    for i in range(n + 1):
        shukei[T[i]] += 1
    for key, num in list(shukei.items()):
        ans += num * (num - 1) // 2
else:
    shukei = defaultdict(int)
    for i in range(k):
        shukei[T[i]] += 1
    for key, num in list(shukei.items()):
        ans += num * (num - 1) // 2
    for i in range(k, n + 1):
        j = i - k
        shukei[T[j]] -= 1
        temp = T[i]
        num = shukei[temp]
        ans += num
        shukei[temp] += 1
print(ans)
