S = input()
K = int(input())
con = 0
for i in S:
    if i == '1':
        con += 1
    else:
        break
if con >= K:
    print((1))
else:
    print(i)
