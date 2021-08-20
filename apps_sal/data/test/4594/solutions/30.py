N = int(input())
moti_list = [int(input()) for i in range(N)]
moti_list.sort(reverse=True)
tower = 1
for j in range(N - 1):
    if moti_list[j] > moti_list[j + 1]:
        tower += 1
print(tower)
