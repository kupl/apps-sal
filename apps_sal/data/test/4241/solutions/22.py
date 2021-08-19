s = input()
t = input()
string_list = []
for i in range(len(s) - len(t) + 1):
    string_list.append(s[i:i + len(t)])
count = 0
max_value = 0
for j in range(len(string_list)):
    for i in range(len(t)):
        if string_list[j][i] == t[i]:
            count += 1
        if max_value < count:
            max_value = count
    count = 0
print(len(t) - max_value)
