N = int(input())
S = list(input())
x = 0
maxi = 0
for i in S:
    if i == 'I':
        x += 1
    else:
        x -= 1
    if x > maxi:
        maxi = x
print(maxi)
