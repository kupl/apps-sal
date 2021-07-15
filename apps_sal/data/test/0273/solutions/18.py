name, surname = input().split()

ans = name[0] + surname[0]
for i in range(len(name)):
    cur_ans = name[:i + 1]
    for j in range(len(surname)):
        cur_ans += surname[:j + 1]
        ans = min(ans, cur_ans)

print(ans)
