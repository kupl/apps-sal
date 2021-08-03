import sys

N = int(input())
L = list(map(int, input().split()))
count = 0
for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            a = L[i]
            b = L[j]
            c = L[k]
            if abs(b - c) < a < b + c and (a != b and a != c and b != c):
                count += 1
print(count)
