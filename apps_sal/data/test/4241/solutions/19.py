s = input()
t = input()
s_len = len(s)
t_len = len(t)
counter = 0
count_max = 0
for i in range(s_len - t_len + 1):
    for j in range(t_len):
        if s[i + j] == t[j]:
            counter += 1
            if counter > count_max:
                count_max = counter
    counter = 0
print((t_len - count_max))

