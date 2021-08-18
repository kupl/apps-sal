def seq(a, new):
    nonlocal count
    for i in range(1, len(a)):
        if a[i] == a[i - 1]:
            new.append(a[i])
    if len(a) > 1:
        count += len(a) - len(new) - 1
    if len(new) == 0:
        return
    else:
        a = new[:]
        new = []
        seq(a, new)


n = int(input())
a = list(map(int, input().split()))
a.sort()
new = []
count = 0
seq(a, new)
print(count)
