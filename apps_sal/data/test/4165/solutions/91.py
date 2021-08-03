# N
N = int(input())
my_list = list(map(int, (input().split(maxsplit=N))))

sorted_list = sorted(my_list, reverse=True)

num = 0
for i in range(1, len(my_list)):
    num += sorted_list[i]

if sorted_list[0] < num:
    answer = 'Yes'
else:
    answer = 'No'

print(answer)
