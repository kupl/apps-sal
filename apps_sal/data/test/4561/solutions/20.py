lst = input().split()
X = int(lst[0])
A = int(lst[1])
B = int(lst[2])
d = B - A
if d <= 0:
    print('delicious')
elif d <= X:
    print('safe')
else:
    print('dangerous')
