N = int(input())
D, X = map(int, input().split())
count = X
for _ in range(N):
    A = int(input())
    count += (D-1) // A + 1
print(count)
