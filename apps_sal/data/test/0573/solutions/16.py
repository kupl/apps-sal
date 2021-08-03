n = int(input())
a = list(map(int, input().split()))
n1, n2 = 0, 0
for i in a:
    if i == 1:
        n1 += 1
    if i == 2:
        n2 += 1
s = min(n2, n1)
n1 -= s
s += n1 // 3
print(s)
