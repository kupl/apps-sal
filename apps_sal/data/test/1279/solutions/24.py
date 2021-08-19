import sys
input = sys.stdin.readline
(n, m) = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
oddA = 0
evenA = 0
for i in a:
    if i % 2:
        oddA += 1
    else:
        evenA += 1
oddB = 0
evenB = 0
for i in b:
    if i % 2:
        oddB += 1
    else:
        evenB += 1
print(min(oddA, evenB) + min(oddB, evenA))
