n = int(input())
s = str(input())

max_result = 0
result = 0


for i in s:
    if i == "I":
        result += 1
        if result > max_result:
            max_result = result
    else:
        result -= 1


print(max_result)
