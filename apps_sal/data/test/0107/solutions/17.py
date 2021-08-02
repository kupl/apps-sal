s = str(input())
f = False
count = 0
for i in s:
    if f:
        if i == '0':
            count += 1
    else:
        if i == '1':
            f = True

if count >= 6:
    print("yes")
else:
    print("no")
