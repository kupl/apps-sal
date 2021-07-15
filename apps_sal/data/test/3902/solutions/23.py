s = input()

possible = [[],[],[False]*10100, [False]*10100]

length = len(s)
possible[2][length-2] = True
possible[3][length-3] = True

for i in range(length-1, 5-1,-1):
    if length - 4 >= i:
        possible[2][i] = (possible[2][i+2] and s[i:i+2] != s[i+2:i+4]) or possible[3][i+2]
    if length - 5 >= i:
        possible[3][i] = possible[2][i+3]
    if length - 6 >= i:
        possible[3][i] = (possible[3][i + 3] and s[i:i+3] != s[i+3:i+6]) or possible[3][i]

output = set()

for i in range(5,10000):
    if possible[2][i]:
        output.add(s[i:i + 2])
    if possible[3][i]:
        output.add(s[i:i + 3])

output_list = sorted(list(output))
print(len(output_list))
for o in output_list:
    print(o)

