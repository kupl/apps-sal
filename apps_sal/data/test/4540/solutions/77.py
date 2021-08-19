n = int(input())
a = [int(i) for i in input().split()]
a.append(0)
a = [0] + a
total = 0
for i in range(1, n + 2):
    total += abs(a[i - 1] - a[i])


def herasu(i):
    ans = total - abs(a[i - 1] - a[i]) - abs(a[i] - a[i + 1]) + abs(a[i - 1] - a[i + 1])
    return ans


for i in range(1, n + 1):
    print(herasu(i))
