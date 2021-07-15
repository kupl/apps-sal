n = int(input())
x_smb = set()
o_smb = set()
flag_yes = True
for i in range(n):
    next_str = list(str(input()))
    x_smb = x_smb | set([next_str[i], next_str[-i-1]])
    for j in sorted(list(set((i, n-i-1))), reverse=True):
        next_str.pop(j)
    o_smb = o_smb | set(next_str)
    if len(x_smb) != 1 or len(o_smb) != 1 or len(x_smb | o_smb) == 1:
        print('NO')
        flag_yes = False
        break
if flag_yes:
    print('YES')
