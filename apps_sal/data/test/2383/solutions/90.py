n = int(input())
a = [int(s) for s in input().split()]
num = 0
current = 1
for i in range(n):
    if a[i] == current:
        current += 1
    else:
        num += 1
print(num) if num != n else print(-1)
