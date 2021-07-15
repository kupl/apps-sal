n, m = map(int, input().split())
data = []
used = [False for i in range(m)]
for i in range(n):
    help = list(map(int, input().split()))
    help = help[1:]
    for elem in help:
        used[elem - 1] = True
if False in used:
    print("NO")
else:
    print("YES")
