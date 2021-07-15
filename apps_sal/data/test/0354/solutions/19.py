glas = ['a', 'e', 'i', 'o', 'u']

s = input()
s1 = input()

if len(s) != len(s1):
    print("No")
    return
else:
    for i in range(len(s)):
        if (s[i] in glas and not s1[i] in glas):
            print("No")
            return
        if not s[i] in glas and s1[i] in glas:
            print("No")
            return
print("Yes")

