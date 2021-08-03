num = int(input())
nu_list = [int(v) for v in input().split()]
count = 0
# print(nu_list)
bool = True
while bool == True:
    for i in range(len(nu_list)):
        if nu_list[i] % 2 != 0:
            bool = False
            break
        else:
            nu_list[i] = nu_list[i] // 2
    if bool == True:
        count += 1
print(count)
