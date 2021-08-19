"""

"""
inp = input().split()
n = int(inp[0])
w = int(inp[1])
cups = sorted(list(map(int, input().split())))
girl = cups[0]
boy = cups[n]
s = 0
s += min(girl, boy / 2) * 3 * n
print(min(s, w))
