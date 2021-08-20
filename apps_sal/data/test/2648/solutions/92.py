from collections import Counter
n = int(input())
A = tuple(map(int, input().split()))
CA = Counter(A)
cu2 = 0
for (k, v) in list(CA.items()):
    cu2 += v - 1
print(len(A) - cu2 - cu2 % 2)
