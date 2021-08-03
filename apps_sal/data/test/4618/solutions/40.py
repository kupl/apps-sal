s = input()
k = int(input())
l = []
for i in range(len(s)):
    for j in range(i + 1, min(i + k + 1, len(s) + 1)):
        l.append(s[i:j])
print(sorted(list(set(l)))[k - 1])
