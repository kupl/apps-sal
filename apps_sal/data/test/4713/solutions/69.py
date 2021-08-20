n = int(input())
s = input()
x = 0
maxx = 0
for i in range(n):
    if s[i] == 'I':
        x += 1
        if maxx < x:
            maxx = x
    else:
        x -= 1
print(maxx)
