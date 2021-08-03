a, k = input().split()
k = int(k)
start = -1
for j in range(len(a)):
    if a[j] != '0':
        start = j
        break
ans = 0
for j in range(len(a) - 1, j, -1):
    if k != 0:
        if a[j] == '0':
            k -= 1
        else:
            ans += 1
    else:
        break

if k == 0:
    print(ans)
else:
    print(len(a) - 1)
