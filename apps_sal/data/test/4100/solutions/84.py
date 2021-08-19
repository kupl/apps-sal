(people_num, start_point, correct_num) = map(int, input().split())
table = [start_point] * people_num
for i in range(correct_num):
    correct_person = int(input())
    table[correct_person - 1] += 1
for j in range(people_num):
    table[j] -= 1 * correct_num
for k in range(people_num):
    if table[k] <= 0:
        print('No')
    else:
        print('Yes')
