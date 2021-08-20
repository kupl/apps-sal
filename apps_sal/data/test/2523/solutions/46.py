s = input()
n = len(s)
key = []
count = 1
for i in range(n - 1):
    if s[i] != s[i + 1]:
        key.append(count)
        count = 1
    else:
        count += 1
key.append(count)
sum_key = sum(key)
ans = 10000000
for i in range(len(key)):
    if i != 0:
        key[i] += key[i - 1]
    ans = min(ans, max(key[i], n - key[i]))
print(ans)
