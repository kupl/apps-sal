n = int(input())
A = list(map(int, input().split()))

s = max(A)
t = sum(A) - s
print(s - t + 1)
