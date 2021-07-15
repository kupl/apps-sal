n=int(input())
x=int(input())
lst=['012','102','120','210','201','021']
n %= 6
str = lst[n]
print(str[x])

