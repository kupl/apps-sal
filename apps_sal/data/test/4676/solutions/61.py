O = input()
E = input()
result = ''
if len(O) == len(E):
    for i in range(len(O)):
        result += O[i] + E[i]
else:
    for i in range(len(E)):
        result += O[i] + E[i]
    result += O[-1]
print(result)
