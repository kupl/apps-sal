x = input()
str_a = x.split(" ")
array = [0] * 10
for s in str_a:
    array[int(s)] += 1
if array[5] == 2 and array[7] == 1:
    print("YES")
else:
    print("NO")
