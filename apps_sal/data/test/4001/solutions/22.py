a = int(input())
b = list(map(int, input().split()))
x = max(b)
for i in range(1, x + 1):
    if x % i == 0:
        b.remove(i)
print(x, max(b))
