N = int(input())
d_list = []
Height = 0
for i in range(N):
    d_list.append(int(input()))
while d_list != []:
    MAX_Value = max(d_list)
    while MAX_Value == max(d_list):
        d_list.remove(MAX_Value)
        if d_list == []:
            break
    Height += 1
print(Height)
