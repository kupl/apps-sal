3

n = int(input())
a = list(map(int, input().split()))

used = set()
reversed(sorted(a))
i = 0
while i < n:
    if a[i] == 0:
        i += 1
    else:
        if a[i] not in used:
            used.add(a[i])
            i += 1
        else:
            a[i] -= 1
print(str(sum(a)))
