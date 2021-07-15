s = input()
k = int(input())
n = len(s)
temp_set = set()
for i in range(n):
    for j in range(i + 1, min(i + k + 1, n + 1)):
        temp_set.add(s[i:j])
temp_list = sorted(list(temp_set))
print(temp_list[k - 1])
