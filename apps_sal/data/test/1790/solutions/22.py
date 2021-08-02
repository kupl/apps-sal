n = int(input())
a = [0] * 101
for i in range(n):
    b = [int(x) for x in input().split()]
    for j in range(1, len(b)):
        a[b[j]] += 1
for i in range(len(a)):
    if a[i] == n:
        print(i, end=" ")
print()
