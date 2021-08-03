n = int(input())
a = list(map(int, input().split()))
d = sum(a) // n
was = [False] * (2 * n)
for i in range(2 * n):
    if was[i]:
        continue
    for j in range(i + 1, 2 * n):
        if was[j]:
            continue
        if a[i] + a[j] == d:
            print(a[i], a[j])
            was[i] = True
            was[j] = True
            break
