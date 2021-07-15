n = int(input())

a = list(map(int, input().split()))
l = []
for i in range(len(a)):
    l.append((i + 1, a[i]))
l.sort(key=lambda x: x[1])
for i in range(n//2):
    print(l[i][0], l[n - i - 1][0])

