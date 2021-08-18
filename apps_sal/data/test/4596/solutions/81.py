N = int(input())
A_list = list(map(int, input().split()))

ans_list = []
temp_ans = 0

for value in A_list:
    temp_value = value
    temp_ans = 0
    while temp_value % 2 == 0:
        temp_value /= 2
        temp_ans += 1

    ans_list.append(temp_ans)

print(min(ans_list))
