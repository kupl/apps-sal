dict = {}
for x in range(int(input())):
    s = input()
    if not s in dict.keys():
        dict[s] = 1
    else:
        dict[s] += 1

print(max(dict.values()))
