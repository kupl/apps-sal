n, p = list(map(int, input().split()))
l_1, r_1 = list(map(int, input().split()))
pre_l, pre_r = l_1, r_1
answer = 0
for i in range(n - 1):
    l, r = list(map(int, input().split()))
    now_shark = [l, r]
    x1 = (r // p - (l - 1) // p) / (r - l + 1)
    x2 = (pre_r // p - (pre_l - 1) // p) / (pre_r - pre_l + 1)
    answer += (1 - (1 - x1) * (1 - x2)) * 2000
    pre_l, pre_r = l, r
x1 = (r_1 // p - (l_1 - 1) // p) / (r_1 - l_1 + 1)
x2 = (pre_r // p - (pre_l - 1) // p) / (pre_r - pre_l + 1)
answer += (1 - (1 - x1) * (1 - x2)) * 2000
print(answer)



