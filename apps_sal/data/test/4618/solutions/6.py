s = input()
k = int(input())
a = []
for i in range(len(s)):
    for j in range(i + 1, len(s) + 1):
        if j - i >= 6:
            break
        a.append(s[i:j])
res = sorted(set(a))
print(res[k - 1])
