n, K = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
k = len(a)

i = 0
while i < len(a):
    if a[i] == a[-1]:
        break
    j = i+1
    while a[i] == a[j]:
        j += 1
    if a[i] + K >= a[j]:
        k -= j - i
    i = j

print(k)
