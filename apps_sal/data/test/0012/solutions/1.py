n = int(input())
s = input()


max_ans = len([x for x in s if x == 'G'])
right = 0
cnt = 0
ans = 0
for i in range(n):
    assigned = False
    for j in range(right, n, 1):
        if s[j] == 'S':
            cnt += 1
        if cnt > 1:
            right = j
            cnt -= 1
            assigned = True
            break
    if not assigned:
        right = n
    # print(i, right)
    ans = max(ans, right - i)
    if s[i] == 'S':
        cnt -= 1
ans = min(ans, max_ans)
print(ans)
