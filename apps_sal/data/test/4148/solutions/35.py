num = int(input())

node = input()
table = list(node)


for i in table:
    aaa = ord('A') + ((ord(i) - (ord('A')) + num) % 26)
    print(chr(aaa), end='')
