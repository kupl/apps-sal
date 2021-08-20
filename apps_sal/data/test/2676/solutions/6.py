def subString(s, n):
    lst = []
    for i in range(n):
        for len in range(i + 1, n + 1):
            lst.append(s[i:len])
    return lst


lst = []
for _ in range(int(input())):
    n = input()
    lst.append(n)
m = int(input())
b = input()
subs = subString(b, m)
uniques = []
count = 0
for i in subs:
    if i not in uniques:
        uniques.append(i)
for i in uniques:
    if i in lst:
        count += 1
print(count)
