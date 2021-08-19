arr = input().split()
a = int(arr[0])
b = int(arr[1])
if a % 2 == 1 and b % 2 == 1:
    if a < b:
        a -= 1
        flag = 1
    else:
        b -= 1
        flag = 2
elif a % 2 == 1:
    a -= 1
    flag = 1
elif b % 2 == 1:
    b -= 1
    flag = 2
elif a > b:
    a -= 1
    flag = 1
else:
    b -= 1
    flag = 2
if flag == 1:
    s = 'a'
else:
    s = 'b'
play = 2
while a > 0 and b > 0:
    if flag == 1:
        if play == 2:
            s += 'b'
            b -= 1
            play = 1
            flag = 2
        else:
            s += 'a'
            a -= 1
            play = 2
    elif play == 2:
        s += 'a'
        a -= 1
        play = 1
        flag = 1
    else:
        s += 'b'
        b -= 1
        play = 2
while a > 0:
    s += 'a'
    a -= 1
while b > 0:
    s += 'b'
    b -= 1
s = list(s)
prev = s[0]
n = len(s)
a = 0
b = 0
for i in range(1, n):
    if s[i] == prev:
        a += 1
    else:
        b += 1
    prev = s[i]
print(str(a) + ' ' + str(b))
