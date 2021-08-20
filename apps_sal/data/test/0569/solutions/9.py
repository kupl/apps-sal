alth = 'abcdefghijklmnopqrstuvwxyz'
n = int(input())
s = input()
temp = [0] * 26
if n > 26:
    print(-1)
else:
    for i in s:
        temp[alth.find(i)] = 1
    print(n - sum(temp))
