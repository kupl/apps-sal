n = int(input())
l = [int(x) for x in input().split()]

d = l[1] - l[0]
for i in range(2, n):
    if l[i] != l[i - 1] + d:
        d = 0
print(l[-1] + d)
