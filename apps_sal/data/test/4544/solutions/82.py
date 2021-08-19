# （i+1 and i and i-1）の合計数が一番多いところを見つける
from collections import Counter
ans = []
N = int(input())
a = list(map(int, input().split()))
num = Counter(a)
for i in set(a):
    ans.append(num[i] + num[i + 1] + num[i - 1])

print(max(ans))
