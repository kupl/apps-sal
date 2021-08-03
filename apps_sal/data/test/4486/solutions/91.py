S = input()
count = 1
str_odd = ''

for i in S:
    if count % 2 == 1:
        str_odd += i
    count += 1

print(str_odd)
