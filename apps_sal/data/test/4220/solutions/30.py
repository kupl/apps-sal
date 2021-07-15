integer = int(input())
string = input()
if len(string) > integer:
    print(string[:integer] + '...')
else:
    print(string)
