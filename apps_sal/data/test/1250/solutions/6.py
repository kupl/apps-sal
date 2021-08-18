sa = int(input())
string = ''
if sa == 1 or sa == 2:
    print("-1")
else:
    for x in range(sa, 0, -1):
        string += str(x)
        string += ' '
    print(string.strip())
