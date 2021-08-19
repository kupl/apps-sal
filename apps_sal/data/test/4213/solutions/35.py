N = int(input())
my_list = list(map(int, input().split(maxsplit=N)))
my_list_sort = sorted(my_list, reverse=True)
answer = my_list_sort[0] - my_list_sort[-1]
print(answer)
