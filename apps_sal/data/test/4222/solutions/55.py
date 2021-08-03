n, k = map(int, input().split())
kl = [[] for i in range(k)]
for i in range(k):
    d = int(input())
    a = list(map(int, input().split()))
    for j in range(d):
        kl[i].append(a[j])
safe = 0
for i in range(1, n + 1):
    for j in range(k):
        if i in kl[j]:
            safe += 1
            break
print(n - safe)
