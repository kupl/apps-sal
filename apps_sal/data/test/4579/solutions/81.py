n = int(input())
result_dict = {}
for i in range(n):
    n = input()
    if n in result_dict.keys():
        result_dict[n] += 1
    else:
        result_dict[n] = 0
print(len(result_dict.keys()))
