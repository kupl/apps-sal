# B - Hina Arare

# N
N = int(input())
my_list = list(input().split())

arare_list = ['P', 'W', 'G', 'Y']
my_list_only = set(my_list)
count = 0

for i in range(0, 4):
    if arare_list[i] in my_list_only:
        count += 1

if count == 3:
    answer = 'Three'
if count == 4:
    answer = 'Four'

print(answer)
