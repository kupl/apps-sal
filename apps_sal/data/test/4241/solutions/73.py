s = input()
t = input()
ans_list = []
for i in range(len(s) - len(t) + 1):
    u = s[i:len(t) + i]
    check_count = 0
    for (a, b) in zip(u, t):
        if a != b:
            check_count += 1
    ans_list.append(check_count)
print(min(ans_list))
