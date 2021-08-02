st_list = list(input())
nu_list = [int(v) for v in st_list]
count = 0
for i in range(len(nu_list)):
    if nu_list[i] == 1:
        count += 1
print(count)
