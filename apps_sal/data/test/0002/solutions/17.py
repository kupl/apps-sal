n = int(input())
size = len(str(n))
num = str(n)[0]
res = (int(num) + 1) * 10 ** (size - 1) - n
print(res)

