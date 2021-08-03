num = input()
Line_1 = input().split(' ')
Line_2 = []
for thing in Line_1:
    Line_2.append(int(thing))
Line_2.sort()
string = ''
for x in range(len(Line_2) - 1):
    string += (str(Line_2[x]))
    string += ' '
string += str(Line_2[-1])
print(string)
