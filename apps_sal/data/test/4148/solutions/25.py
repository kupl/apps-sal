n = int(input())
s = input()
alp = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"

for i in range(len(s)):
    print(alp[alp.index(s[i]) + n], end="")
print()
