s = input()
k = int(input())
li = []
for i in range(len(s)):
    for j in range(i + 1, len(s) + 1):
        if j - i <= 6:
            li += [s[i:j]]
li2 = set(li)
li3 = sorted(li2)
print(li3[k - 1])
