n, m = list(map(int, input().split()))
ar = []
for _ in range(n):
    ar.append(input())
ans1 = ''
ans2 = ''
kek = set()
for i in range(n):
    for j in range(i + 1, n):
        if ar[i] == ar[j][::-1]:
            ans1 += ar[i]
            ans2 = ar[j] + ans2
            kek.add(ar[i])
for i in range(n):
    if ar[i] == ar[i][::-1] and ar[i] not in kek:
        ans1 += ar[i]
        break
print(len(ans1) + len(ans2))
print(ans1 + ans2)
