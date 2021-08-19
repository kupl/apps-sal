n = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
a.append(2)
cnt = 0
ans = 0
for i in range(len(a)):
    if a[i] > 3:
        cnt += 1
    else:
        ans += cnt // 3
        cnt = 0
print(ans)
