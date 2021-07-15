f = {'0' : '23', '1' : '10', '2' : '30', '3' : '11', '4' : '13', '5' : '12', '6' : '31', '7' : '33', '8' : '32', '9' : '21'}
n = input()
s = ''
for i in n: s += f[i]
def check(s):
    for i in range(len(s)):
        if s[i] != s[-i - 1]: return 0;
    return 1;
print('Yes' if check(s) else 'No')

