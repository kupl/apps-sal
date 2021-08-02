n = int(input())
l = [int(x) for x in input().split()]
print(l[1] - l[0], l[n - 1] - l[0])
for i in range(1, n - 1):
    print(min(l[i] - l[i - 1], l[i + 1] - l[i]), max(l[i] - l[0], l[n - 1] - l[i]))
print(l[n - 1] - l[n - 2], l[n - 1] - l[0])
