(health, attacks) = map(int, input().split())
num_list = [num for num in map(int, input().split())]
num_list.sort(reverse=True)
print(sum(num_list[attacks:]))
