num = int(input())
nums = input()
statement = [int(i) for i in nums.split()]
log = {}
group_num = {}
anchor = 1
total = num
status = 'Possible'
ans = []
for (i, s) in enumerate(statement):
    if s not in log or group_num[s] == 0:
        log[s] = anchor
        anchor += 1
        group_num[s] = num - s
        total -= group_num[s]
        if total < 0:
            status = 'Impossible'
            break
    ans.append(log[s])
    group_num[s] -= 1
print(status)
if status == 'Possible':
    for i in range(num - 1):
        print(ans[i], end=' ')
    print(ans[num - 1])
