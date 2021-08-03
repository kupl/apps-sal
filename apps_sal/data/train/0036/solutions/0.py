n = int(input())
a = list(map(int, input().split()))
k = []
for i in range(n):
    for j in range(a[i]):
        k.append(i + 1)
m = int(input())
b = list(map(int, input().split()))
for i in b:
    print(k[i - 1])
