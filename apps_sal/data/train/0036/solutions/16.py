n = int(input())
a = [0]
b = list(map(int, input().split()))
for i in range(len(b)):
    for j in range(b[i]):
        a.append(i + 1)
n = int(input())
b = list(map(int, input().split()))
for i in range(len(b)):
    print(a[b[i]])
