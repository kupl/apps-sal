import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
(n, k) = list(map(int, input().split()))
A = []
for (i, light) in enumerate(list(map(int, input().split()))):
    A.append((light, i))
A.sort(reverse=True)
print(A[k - 1][0])
out = [A[i][1] + 1 for i in range(k)]
print(' '.join(map(str, out)))
