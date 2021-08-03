import re
input()
ds = "L" + input() + "R"
res = len(re.findall("R(?:\.\.)*\.L", ds)) + sum([len(s) - 2 for s in re.findall("L\.*R", ds)])
print(res)
