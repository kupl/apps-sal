n = int(input())
a = list(map(int, input().split()))
unresolved = []
days = 0
for i in range(n):
    unresolved.append(a[i])
    if max(unresolved) > i + 1:
        continue
    else:
        days += 1
        continue
print(days)
