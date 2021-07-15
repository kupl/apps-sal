a = {'a', 'e', 'i', 'o', 'u'}


s = input()
k = input()
if len(s) != len(k):
    print("No")
    return
for i in range(len(s)):
    if not ((s[i] in a and k[i] in a) or (s[i] not in a and k[i] not in a)):
        print("No")
        return
print("Yes")
