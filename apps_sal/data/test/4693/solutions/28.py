S_list = list(map(int, input().split()))

add = S_list[0] + S_list[1]
if add >= 10:
    result = "error"
else:
    result = add
print(result)
