s = input()
t = input()
ls = list(s)
lt = list(t)
result = 0
for data in range(len(ls)):
    if ls[data] != lt[data]:
        result += 1
print(result)

