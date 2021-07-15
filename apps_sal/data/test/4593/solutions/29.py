X = int(input())
res_list = [1]

for i in range(1,X):
    for j in range(2,X):
        if i ** j <= X:
            res_list.append(i ** j)
        else:
            break

print(max(res_list))
