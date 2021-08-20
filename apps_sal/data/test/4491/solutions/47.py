N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))[::-1]
l = []
for i in range(N):
    l.append(sum(A[:N - i]) + sum(B[:i + 1]))
print(max(l))
