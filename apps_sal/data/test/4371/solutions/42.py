s = list(input())
s_len = len(s)
s_list = []
for i in range(0, s_len - 2):
    s_list.append(abs(753 - int(s[i] + s[i + 1] + s[i + 2])))
print(min(s_list))
