n = int(input())
s = input()
ss = s
while ss.count('()'):
    ss = ss.replace('()', '')
left, right = ss.count('('), ss.count(')')
print('(' * right + s + ')' * left)
