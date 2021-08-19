n = int(input())
s = input()
a = [set()]
k = 0
for i in range(len(s)):
    if s[i].upper() == s[i] and a[-1] != set():
        k += 1
        a.append(set())
    elif s[i].lower() == s[i] and s[i] not in a[-1]:
        a[-1].add(s[i])
print(max([len(x) for x in a]))
