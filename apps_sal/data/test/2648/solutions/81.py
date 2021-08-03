from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

dict = defaultdict(int)

for a in A:
    dict[a] += 1

num = [0] * 2
for v in dict.values():
    num[v % 2] += 1

if num[0] % 2 == 0:
    print(sum(num))
else:
    print(sum(num) - 1)
