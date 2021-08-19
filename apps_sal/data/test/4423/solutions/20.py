N = int(input())
my_list = []
for i in range(N):
    sp = input().split()
    sp[1] = int(sp[1])
    sp.insert(0, i + 1)
    my_list.append(sp)
my_list.sort(key=lambda x: x[2], reverse=True)
my_list.sort(key=lambda x: x[1])
for i in my_list:
    print(i[0])
