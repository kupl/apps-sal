n = int(input())
d, x = map(int, input().split())
a = [int(input()) for i in range(n)]
count = 0
for i in a:
    count += d // i + (0 if d % i == 0 else 1)
print(count + x)
