n = int(input())
a_list = [int(x) for x in input().split()]
temp_list = [0] * (n + 1)
for i in range(1, n + 1):
    temp_list[i] = a_list[i - 1] + temp_list[i - 1]
l = 1
r = 3
ans = temp_list[-1]
for m in range(2, n - 1):
    gap_min = abs(temp_list[m] - temp_list[l] - (temp_list[l] - temp_list[0]))
    while l < m:
        l += 1
        gap = abs(temp_list[m] - temp_list[l] - (temp_list[l] - temp_list[0]))
        if gap < gap_min:
            gap_min = gap
        else:
            l -= 1
            break
    else:
        l -= 1
    gap_min = abs(temp_list[n] - temp_list[r] - (temp_list[r] - temp_list[m]))
    while r < n:
        r += 1
        gap = abs(temp_list[n] - temp_list[r] - (temp_list[r] - temp_list[m]))
        if gap < gap_min:
            gap_min = gap
        else:
            r -= 1
            break
    else:
        r -= 1
    num_list = sorted([temp_list[l] - temp_list[0], temp_list[m] - temp_list[l], temp_list[r] - temp_list[m], temp_list[n] - temp_list[r]])
    ans_temp = num_list[3] - num_list[0]
    if ans_temp < ans:
        ans = ans_temp
print(ans)
