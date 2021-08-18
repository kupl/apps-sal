from collections import Counter

N = int(input())
S = [''.join(sorted(input())) for _ in range(N)]

num = Counter(S)

result = sum(x * (x - 1) // 2 for x in num.values())
print(result)
