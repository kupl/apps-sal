s = str(input())
K = int(input())
str_list = set()
for i in range(len(s) + 1):
    for j in range(i + 1, i + K + 1):
        if j > len(s):
            break
        str_list.add(s[i:j])
str_list = list(str_list)
str_list.sort()
print(str_list[K - 1])
