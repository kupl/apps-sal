n = int(input())
s = input().split()
initial_pos = 0
ans = 0
ans_list = []
l = set()
for i in range(n):
    if s[i] in l:
        ans += 1
        ans_list.append([initial_pos + 1, i + 1])
        initial_pos = i + 1
        l = set()
    else:
        l.add(s[i])
if ans == 0:
    print(-1)
else:
    if not ans_list[-1][1] == n:
        ans_list[-1][1] = n
    print(ans)
    for i in ans_list:
        print(' '.join(str(e) for e in i))
