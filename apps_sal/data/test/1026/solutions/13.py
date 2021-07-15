n = int(input())
line = list(map(int, input().split()))
for i in range(n):
    line[i] -= i
cou = dict()
for i in range(n):
    if line[i] in cou:
        cou[line[i]].append(i)
    else:
        cou[line[i]] = [i]
ans = -1
for i in cou:
    t_ans = i * len(cou[i])
    for el in cou[i]:
        t_ans += el
    ans = max(ans, t_ans)
print(ans)
