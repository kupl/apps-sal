n = int(input())
s = input()
ans = 0
for i in range(n):
    if s[i] == 'x' and (i == 0 or s[i - 1] != 'x'):
        j = i
        while j + 1 < n:
            if s[j + 1] == 'x':
                j += 1
            else:
                break
        sz = j - i + 1
        ans += max(0, sz - 2)
print(ans)
