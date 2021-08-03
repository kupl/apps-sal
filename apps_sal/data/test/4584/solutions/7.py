n = int(input())
a = list(map(int, input().split()))
l = [0] * (n + 1)

for i in a:
    l[i] += 1

for i in range(1, n + 1):
    print(l[i])
