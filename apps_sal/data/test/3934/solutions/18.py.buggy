t = int(input())
lst = [[] for c in range(t + 1)]
for c in range(t - 1):
    m, n = map(int, input().split())
    lst[m].append(n)
    lst[n].append(m)
for c in range(len(lst)):
    if len(lst[c]) == 2:
        print("NO")
        return
print("YES")
