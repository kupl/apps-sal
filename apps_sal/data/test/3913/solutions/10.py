# while True:
n = int(input())
mark = [0] * 26
notinclude = [0] * 10001
s = input()
t = int(input())
data = [input() for _ in range(t)]
for i in s:
    if i != '*':
        mark[ord(i) - 97] = 1
sets = {}
for j in range(t):
    sets[j] = set()
    for i in range(n):
        if s[i] == '*':
            if mark[ord(data[j][i]) - 97] == 0:
                sets[j].add(data[j][i])
            else:
                notinclude[j] = 1
        elif s[i] != data[j][i]:
            notinclude[j] = 1

ans = set(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
temp = 0
# print(sets)
for i in sets:
    if len(sets[i]) and notinclude[i] == 0:
        temp = 1
        ans = ans & sets[i]
# print(ans)
print(0 if temp == 0 else len(ans))

''' input
2
**
3
ba
ba
ba

'''
