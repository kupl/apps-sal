n = int(input())
a = list(map(int, input().split()))

num = 1
for i in range(n):
    if a[i] == num:
        num += 1
print(n - (num - 1) if num != 1 else -1)
