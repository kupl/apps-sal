input()
a = [int(i)for i in input().split()]
a = [0] + a + [0]
b = int(input())
while b > 0:
    c = [int(i)for i in input().split()]
    a[c[0] - 1] += c[1] - 1
    a[c[0] + 1] += a[c[0]] - c[1]
    a[c[0]] = 0
    b -= 1
for i in range(len(a) - 2):
    print(a[i + 1])
