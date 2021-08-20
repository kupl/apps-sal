n = int(input())
s = input()
sl = [i for i in s]
c = 0
x = s.find('xxx')
while x != -1:
    c += 1
    sl.pop(x)
    temp = ''
    for i in sl:
        temp += i
    x = temp.find('xxx')
print(c)
