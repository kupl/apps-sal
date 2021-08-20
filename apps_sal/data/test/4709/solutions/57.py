S_list = list(input().split())
if S_list[1] == '+':
    result = int(S_list[0]) + int(S_list[2])
else:
    result = int(S_list[0]) - int(S_list[2])
print(result)
