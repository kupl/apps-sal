n = int(input())
for i in range(n):
    line = input()
    result = 0
    if len(line) >= 5 and line[0:5] == 'miao.':
        result += 1
    if len(line) >= 5 and line[-5:] == 'lala.':
        result += 2
    if result == 2: print("Freda's")
    elif result == 1: print("Rainbow's")
    else: print("OMG>.< I don't know!")

