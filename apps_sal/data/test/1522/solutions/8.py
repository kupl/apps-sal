ans = 0
n = int(input())
keys = [0 for i in range(30)]
s = input()
for i in range(n - 1):
    keys[ord(s[2 * i].capitalize()) - ord('A')] += 1
    if keys[ord(s[2 * i + 1]) - ord('A')] == 0:
        ans += 1
    else:
        keys[ord(s[2 * i + 1]) - ord('A')] -= 1
print(ans)
