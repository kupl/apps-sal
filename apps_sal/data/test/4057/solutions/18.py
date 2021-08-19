n = int(input())
a = [int(i) for i in input().split()]
b = [0] * 101
for i in range(n):
    b[a[i]] += 1
print(max(b))
