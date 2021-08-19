# B - Christmas Eve Eve

#  N
N = int(input())
my_list = []

for i in range(0, N):
    my_list.append(int(input()))

my_list = sorted(my_list, reverse=True)
my_list[0] = int(my_list[0] / 2)
answer = sum(my_list)

print(answer)
