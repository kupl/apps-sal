l1 = [0] * 101
l2 = [0] * 101
n = int(input())
for li in range(n):
    (x, y) = input().split(' ')
    a = int(x)
    b = int(y)
    l1[a] = 1
    l2[b] = 1
print(min(sum(l1), sum(l2)))
