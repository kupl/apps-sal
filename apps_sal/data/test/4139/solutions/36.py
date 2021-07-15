N = int(input())
count = 0
num_list = [["3", "5", "7"]]
 
for i in range(2, 10):
    temp = []
    for j in num_list[-1]:
        for k in ["3", "5", "7"]:
            l = k + j
            if N >= int(l) and "3" in l and "5" in l and "7" in l:
                count += 1
            temp.append(l)
    num_list.append(temp)
 
print(count)
