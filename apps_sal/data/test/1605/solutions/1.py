s = input()
a = []
for c in s:
    a.append(ord(c) - ord('a'))
cnt = [[0, 0], [0, 0]]
ans = [0, 0]
for i in range(len(a)):
    cnt[a[i]][i % 2] += 1
    ans[0] += cnt[a[i]][i % 2]
    ans[1] += cnt[a[i]][1 - i % 2]
print(ans[1], ans[0])
