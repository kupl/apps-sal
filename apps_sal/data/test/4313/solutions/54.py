n = int(input())
v_list = [int(i) for i in input().split()]
c_list = [int(i) for i in input().split()]
total_list = []

for i in range(n):
    total_list.append(v_list[i] - c_list[i])

total_list.sort(reverse=True)
# print(total_list)

sum = 0
for i in total_list:
    if i > 0:
        sum += i
    else:
        break

print(sum)
