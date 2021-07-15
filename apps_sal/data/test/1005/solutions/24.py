t = int(input())
ans = []
for _ in range(t):
    n, k, d = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    var = []
    for g in range(n - d + 1):
        var.append(set(a[g:g + d]))
    ans.append(min([len(x) for x in var]))
print('\n'.join([str(x) for x in ans]))

