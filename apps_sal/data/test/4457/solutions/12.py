from operator import itemgetter

N = int(input())
A = list(map(int, input().split()))

B = []
for i, a in enumerate(A):
    B.append((i, a))

B.sort(reverse=True, key = itemgetter(1))

score = 0
for n, (i, b) in enumerate(B):
    score += b*n+1

print(score)
for i, _ in B:
    print(i+1, end=' ')
print()
