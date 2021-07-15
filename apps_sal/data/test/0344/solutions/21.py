s = input().strip()
vowels = ['a', 'e', 'i', 'o', 'u']
val = True
for i in range(len(s) - 1):
    if s[i] not in vowels and s[i] != 'n':
        if s[i+1] not in vowels:
            val = False
            break
if s[-1] not in vowels and s[-1] != 'n':
    val = False
if val:
    print("YES")
else:
    print("NO")
