S = input()
alpahbet = 'abcdefghijklmnopqrstuvwxyz'
string_list = []
ans = 'None'
for s in S:
    if s not in string_list:
        string_list.append(s)
for a in alpahbet:
    if a not in string_list:
        ans = a
        break
print(ans)
