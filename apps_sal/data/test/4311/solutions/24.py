s = int(input())

if s == 1 or s == 2:
    print(4)
    return

def function(n):
    if n % 2 == 0:
        return int(n/2)
    else:
        return int(n*3+1)
i = 0
count = 0
a = []
a.append(s)
while count < 2:
    a.append(function(a[i]))
    if a[i] == 4:
        count += 1
    i += 1
print(i)
