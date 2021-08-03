lst = input().split()

for i in range(3):
    if lst.count(lst[i]) == 1:
        print(lst[i])
        break
