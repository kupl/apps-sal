s = list(input())
K = int(input())
sub_list = []
for i in range(1, min(K + 1, len(s) + 1)):
    for j in range(len(s) - i + 1):
        sub = ''.join(s[j:j + i])
        if sub not in sub_list:
            sub_list.append(sub)
sub_list.sort()
print(sub_list[K - 1])
