n = int(input())
string = input()
numbers = string.split('0')
a = ''
for x in numbers:
    a += str(len(x))
a = int(a)
print(a)
