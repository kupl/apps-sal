# B - Traveling AtCoDeer Problem

# N
N = int(input())
my_list = list(map(int, input().split(maxsplit=N)))

my_list_sort = sorted(my_list)
answer = my_list_sort[-1] - my_list_sort[0]

print(answer)
