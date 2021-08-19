n = int(input())
a = list(map(int, input().split()))
a.sort()
ans = []
for i in range(n):
    if i % 2 == 0:
        ans.append(str(a[i // 2]))
    else:
        ans.append(str(a[-i // 2]))
print(' '.join(ans))
