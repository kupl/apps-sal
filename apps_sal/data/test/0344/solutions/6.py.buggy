s = input()
vo = ['a', 'e', 'i', 'o', 'u']
for i in range(0, len(s) - 1):
    if s[i] not in vo:
        if s[i] == 'n':
            continue
        else:
            if s[i + 1] not in vo:
                print("NO")
                return
if s[len(s) - 1] not in vo and s[len(s) - 1] != 'n':
    print("NO")
else:
    print("YES")
