a = list(input())
vowel = ['a', 'e', 'o', 'u', 'i']
isit = 1
for i in range(len(a)):
    if a[i] not in vowel and a[i] != 'n':
        if i + 1 < len(a):
            if a[i + 1] not in vowel:
                isit = 0
        else:
            isit = 0
if isit:
    print("YES")
else:
    print("NO")
