from collections import Counter

N = int(input())
A = list(map(int, input().split()))

B = []
for a in A:
    B.append(a-1)
    B.append(a)
    B.append(a+1)
C = Counter(B)

print(C.most_common()[0][1])
