N = int(input())
A_list = list(map(int, input().split()))
A_dict = dict()
for a in A_list:
    if A_dict.get(a) is None:
        A_dict[a] = 1
    else:
        A_dict[a] += 1
ans = 0
for key, val in list(A_dict.items()):
    temp = 0
    if A_dict.get(key - 1) is not None:
        temp += A_dict.get(key - 1)
    if A_dict.get(key) is not None:
        temp += A_dict.get(key)
    if A_dict.get(key + 1) is not None:
        temp += A_dict.get(key + 1)
    ans = max(temp, ans)
print(ans)
