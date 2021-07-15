S = input().split()

my_list = []

for i in range(len(S)):
    S[i] = S[i].title()
    my_list.append(S[i][0])

print(my_list[0]+my_list[1]+my_list[2])
