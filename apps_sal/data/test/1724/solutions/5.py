m = int(input())
listValue = input().split()
x = input().rstrip('\n')

values = [int(v) for v in listValue]
reverse_x = list(x)
reverse_int = [int(s) for s in reverse_x]
reverse_list = [0] * m
sum_list = 0
for i in range(m):
    if reverse_x[i] == '1':
        reverse_list[i] = max(reverse_list[i - 1] + values[i], sum_list)
    else:
        reverse_list[i] = reverse_list[i - 1]
    sum_list += values[i]

print(reverse_list[-1])

