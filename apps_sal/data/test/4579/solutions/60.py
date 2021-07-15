N = int(input())


set_list = {}

for i in range(N):
    s = input()
    set_list[s] = True
print(len(set_list.keys()))
