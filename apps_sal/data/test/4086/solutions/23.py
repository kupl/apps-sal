n = int(input())
a = list(map(int, input().split()))
new = []
was = set()
for i in range(n - 1, -1, -1):
    if a[i] not in was:
        new.append(a[i])
        was.add(a[i])
print(len(new))
for i in range(len(new) - 1, -1, -1):
    print(new[i], end=' ')
