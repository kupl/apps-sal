n = int(input())
s = input()
s_ = s

while s_.count('()'):
    s_ = s_.replace('()', '')

l = s_.count(')')
r = len(s_) - l

ans = '(' * l + s + ')' * r
print(ans)
