N = int(input())
A_ls = []
for i in range(N):
    A_ls.append(int(input()))
sorted_A_ls = sorted(A_ls, reverse=True)
first_val = sorted_A_ls[0]
second_val = sorted_A_ls[1]

for val in A_ls:
    if val == first_val:
        print(second_val)
    else:
        print(first_val)
