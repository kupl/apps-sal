N = int(input())
D, X = list(map(int, input().split()))
sum = 0
for i in range(N):
    A = int(input())
    eat = 1 + (D - 1) // A
    sum += eat
print((X + sum))
