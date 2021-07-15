n = int(input())
s = input()

ans = n
used = [False for i in range(n)]
for i in range(1, n):
    if not used[i - 1] and (s[i] == 'R' and s[i - 1] == 'U' or s[i] == 'U' and s[i - 1] == 'R'):
        ans -= 1
        used[i] = True
        used[i - 1] = True
print(ans)

