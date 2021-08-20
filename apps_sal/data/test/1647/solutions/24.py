links = [{i} for i in range(26)]
spells = []
count = 0
n = int(input())
s1 = input()
s2 = input()
for i in range(0, n):
    n1 = ord(s1[i]) - 97
    n2 = ord(s2[i]) - 97
    if n1 != n2 and (not n2 in links[n1]):
        links[n1] = links[n1].union(links[n2])
        links[n2] = links[n2].union(links[n1])
        for j in links[n1]:
            if j != n1:
                links[j] = links[n1].union(links[j])
        count = count + 1
        spells.append(chr(97 + n1) + ' ' + chr(97 + n2))
print(count)
for i in spells:
    print(i)
