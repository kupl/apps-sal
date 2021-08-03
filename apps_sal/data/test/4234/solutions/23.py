n = int(input())
s = input().strip()
prev = s[0]
ans = [s[0]]
k = 0
for i in range(1, n):
    if (k + i) % 2 == 1 and s[i] == prev:
        k += 1
        continue
    else:
        ans.append(s[i])
        prev = s[i]
if len(ans) % 2 == 1:
    ans.pop()
print(n - len(ans))
print(''.join(ans))
