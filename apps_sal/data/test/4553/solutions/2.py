(a, b) = map(int, input().split())
s = input()
A = s[:a]
con = s[a]
B = s[-b:]
flg = True
num = [str(x) for x in range(10)]
num = set(num)
for x in A:
    if x not in num:
        flg = False
for x in B:
    if x not in num:
        flg = False
if con != '-':
    flg = False
print('Yes' if flg else 'No')
