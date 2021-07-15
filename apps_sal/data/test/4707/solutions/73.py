s1,s2,s3 = map(int, input())

number_list = [s1,s2,s3]

counter = 0

for i in range(len(number_list)):
    if number_list[i] == 1:
        counter += 1
print(counter)
