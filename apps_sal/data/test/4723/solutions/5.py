s = list(input())
t = list(input())
num = len(t)

fail = 'UNRESTORABLE'
flag = False
ans = []
count_out = 0

for i in range(len(s)):
    start = i
    end = i + len(t)
    if (end > len(s)):
        break
    tar = s[start:end]
    index = 0
    name_flag = True

    for a, b in zip(tar, t):
        if (a == b):
            pass
        elif (a == '?'):
            tar[index] = str(b)
        else:
            name_flag = False
            break

        index += 1

    if (name_flag is False):
        ans.append(['z'] * len(s))
        count_out += 1
    else:
        pre_org = s[:start]
        post_org = s[end:]

        tar_mod = pre_org + tar + post_org
        ans.append(tar_mod)

if (count_out == (len(s) - len(t) + 1)):
    print(fail)
else:
    ans_s = sorted(ans)
    aa = ans_s[0]
    a2 = ''.join(aa)
    a3 = a2.replace('?', 'a')
    print(a3)
