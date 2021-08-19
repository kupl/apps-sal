N = int(input())
i = 1
result = 0
while i <= N:
    i_l = len(str(i))
    if i_l % 2 != 0:
        result += 1
    i += 1
print(result)
