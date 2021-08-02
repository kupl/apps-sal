n = int(input())
b = list(map(int, input().split()))
a = []

a.append(b[0])
for i in range(1, n - 1):
    if b[i - 1] < b[i]:
        a.append(b[i - 1])
    else:
        a.append(b[i])
a.append(b[n - 2])
print(sum(a))
