list_s = list(input())
for i in range(0, len(list_s)):
    if list_s[i] == 'U' or list_s[i] == 'D': continue
    elif (i % 2 == 0 and list_s[i] == 'R') or (i % 2 != 0 and list_s[i] == 'L'): continue
    else: print("No")
    return
print("Yes")
