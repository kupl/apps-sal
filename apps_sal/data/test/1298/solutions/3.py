n = int(input())
str = input()
a = str.count("0")
b = str.count("1")
if a-b > 0 :
    print(a-b)
else:
    print(b-a)

