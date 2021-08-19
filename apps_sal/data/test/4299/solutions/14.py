n = input()
nn = n[-1]
a = ['2', '4', '5', '7', '9']
b = ['0', '1', '6', '8']
c = ['3']
if nn in a:
    ans = 'hon'
elif nn in b:
    ans = 'pon'
else:
    ans = 'bon'
print(ans)
