n = int(input())
h_list = list(map(int, input().split()))
a_dict = dict()
b_dict = dict()
for i in range(n):
    a = h_list[i] + i
    b = i - h_list[i]
    if not a in a_dict:
        a_dict[a] = 1
    else:
        a_dict[a] += 1
    if not b in b_dict:
        b_dict[b] = 1
    else:
        b_dict[b] += 1
count = 0
for a in a_dict:
    if a in b_dict:
        count += a_dict[a] * b_dict[a]
print(count)
