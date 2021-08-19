s = input()
t = input()
match_index = 51
for i in range(len(s) - len(t) + 1):
    s_tmp = s[i:i + len(t)]
    for j in range(len(t)):
        if s_tmp[j] == t[j] or s_tmp[j] == "?":
            pass
        else:
            break
    else:
        match_index = i

if match_index == 51:
    print("UNRESTORABLE")
else:
    s_replace = ""
    for i in range(match_index):
        s_replace += s[i]
    s_replace += t
    for i in range(match_index + len(t), len(s)):
        s_replace += s[i]

    # s[match_index:match_index + len(t)] = t
    res = ""
    for i in s_replace:
        if i == "?":
            res += "a"
        else:
            res += i
    print(res)
