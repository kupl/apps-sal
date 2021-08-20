num = int(input())
digs = input()
num_8 = sum((1 for i in digs if i == '8'))
print(min(num_8, num // 11))
