n, m = map(int, input().split())
ls = sorted(list(map(int, input().split())))
su, j, arr = 0, 0, []
for i in range(1, m + 1):
    if j < n and i == ls[j]:
        j += 1
        continue
    su = su + i
    if su > m:
        break
    arr.append(i)

print(len(arr))


for j in arr:
    print(j, end=" ")
