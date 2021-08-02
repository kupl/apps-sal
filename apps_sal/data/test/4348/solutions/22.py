n, k = map(int, input().split())
s = input()
alth = "abcdefghijklmnopqrstuvwxyz"
chars = [0] * 26
chars2 = [0] * 26
for i in range(n):
    chars[alth.find(s[i])] += 1
for i in range(26):
    if k <= 0:
        break
    chars2[i] = min(chars[i], k)
    k -= chars[i]

for i in range(n):
    if chars2[alth.find(s[i])] == 0:
        print(s[i], end="")
    else:
        chars2[alth.find(s[i])] -= 1
