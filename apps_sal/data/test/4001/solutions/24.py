n = int(input())
A = list(map(int, input().split()))
x = max(A)
for i in range(1, x + 1):
    if x % i == 0:
        A.remove(i)
y = max(A)
print(x, y)
