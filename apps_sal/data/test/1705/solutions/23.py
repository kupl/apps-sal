n = int(input())
a = [int(item) for item in input().split()]
(left, right) = (a.count(0), a.count(1))
(l, r) = (0, 0)
for i in range(n):
    if a[i] == 0:
        l += 1
    else:
        r += 1
    if l == left or r == right:
        print(i + 1)
        break
