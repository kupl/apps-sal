n = int(input())
a = [int(v) for v in input().split()]
for i in range(1, len(a) - 1):
    if a[i - 1] == 1 and a[i + 1] == 1:
        a[i] = 1
print(sum(a))
