c = int(input())
s = {}
for i in range(c):
    newI = input()
    if newI not in s:
        s[newI] = 1
    else:
        s[newI] += 1
print(max(s.values()))
