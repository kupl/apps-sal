n = int(input())
string = input()
count = 0
i = n
while i < len(string):
    flag = False
    if string[i - 1] == string[i - 2] and string[i - 2] == string[i - 3] and i >= 3:
        flag = True
    if flag:
        count += 1
    i += n
print(count)
