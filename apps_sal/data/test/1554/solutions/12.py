n = int(input())
a = list(map(int, input().split()))
sub = set()
starts = list()
starts.append(1)
for i in range(n):
    if a[i] in sub:
        sub = set()
        starts.append(i + 2)
    else:
        sub.add(a[i])
l = len(starts)
if l == 1:
    print(-1)
else:
    print(l - 1)
    for i in range(l - 2):
        print(starts[i], starts[i + 1] - 1)
    print(starts[l - 2], n)
