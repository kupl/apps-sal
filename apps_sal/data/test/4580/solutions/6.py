N = int(input())
a = list(map(int, input().split()))
color = []
rainbow = 0
for i in range(N):
    if 1 <= a[i] <= 399:
        color.append('gray')
    elif 400 <= a[i] <= 799:
        color.append('brown')
    elif 800 <= a[i] <= 1199:
        color.append('green')
    elif 1200 <= a[i] <= 1599:
        color.append('sky')
    elif 1600 <= a[i] <= 1999:
        color.append('blue')
    elif 2000 <= a[i] <= 2399:
        color.append('yellow')
    elif 2400 <= a[i] <= 2799:
        color.append('orange')
    elif 2800 <= a[i] <= 3199:
        color.append('red')
    else:
        rainbow += 1
        color.append('all')
if len(set(color)) == 1 and rainbow > 0:
    mini = 1
elif rainbow == 0:
    mini = len(set(color))
else:
    mini = max(1, len(set(color)) - 1)
if rainbow > 1:
    maxi = len(set(color)) + rainbow - 1
else:
    maxi = len(set(color))
print(mini, maxi)
