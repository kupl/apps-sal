n, k = map(int, input().split())
s = input()
num = dict()
all1 = []
ans = 1000000000000
for i in range(65, 65 + k):
    all1.append(chr(i))
for i in range(n):
    if not s[i] in num:
        num[s[i]] = 1
    else:
        num[s[i]] += 1
for i in range(k):
    if all1[i] not in num:
        ans = 0
        break
    ans = min(ans, num[all1[i]])
print(ans * k)
