n  = int(input())
L = list(map(int, input().split())) + [0]
ans = 0
ans_cur = 0
cur_old = 0
cur = 1
for i in range(1, len(L)):
    if L[i] == L[i - 1]:
        cur += 1
    else:
        ans_cur = min(cur, cur_old)
        if ans_cur > ans:
            ans = ans_cur
        cur_old = cur
        cur = 1
        ans_cur = 0

print(ans * 2)
