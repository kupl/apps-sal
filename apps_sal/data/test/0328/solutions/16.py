n = int(input())
(a, b) = list(map(int, input().split()))
max = a + b
for i in range(n - 1):
    (a, b) = list(map(int, input().split()))
    if a + b > max:
        max = a + b
print(max)
