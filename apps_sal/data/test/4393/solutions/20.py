n = int(input())
s = input()
itog = ""
i = 0
k = 1
while i < len(s):
    itog += (s[i])
    i += k
    k += 1
print(itog)
