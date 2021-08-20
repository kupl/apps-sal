n = int(input())
num_list = []
num_odd_list = []
for i in range(1, n + 1):
    num_list.append(i)
for j in num_list:
    if 10 <= j < 100 or 1000 <= j < 10000 or 100000 <= j < 1000000:
        num_odd_list.append(j)
print(len(num_list) - len(num_odd_list))
