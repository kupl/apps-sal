import re
cost = 0
inp = input().split(' ')
string = input()
count0 = re.findall('0+', string)
if count0 and int(inp[1]) < int(inp[2]):
    cost += (len(count0) - 1) * int(inp[1]) + int(inp[2])
else:
    cost += len(count0) * int(inp[2])
print(cost)
