n_k = list(map(int, input().split()))
numbers = list(map(int, input().split()))

output = 0
for i in range(len(numbers)):
    i_str = str(numbers[i])
    lucky = 0
    for j in range(len(i_str)):
        if i_str[j] == '4' or i_str[j] == '7':
            lucky += 1
    if lucky <= n_k[1]:
        output += 1
print(output)
