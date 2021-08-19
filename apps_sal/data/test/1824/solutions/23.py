n = int(input())
a = sorted(map(int, input().split(' ')))
b = sorted(map(int, input().split(' ')))
c = sorted(map(int, input().split(' ')))
for i in range(len(a)):
    if i == n - 1 or a[i] != b[i]:
        print(a[i])
        break
for i in range(len(b)):
    if i == n - 2 or b[i] != c[i]:
        print(b[i])
        break
