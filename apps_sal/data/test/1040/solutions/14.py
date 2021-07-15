n = int(input())
s = input()
ls = []
for i in range(n):
    ls.append(s[i])
    if len(ls) > 2:
        if ls[-3] == "f" and ls[-2] == "o" and ls[-1] == "x":
            n-=3
            ls.pop()
            ls.pop()
            ls.pop()
print(n)

