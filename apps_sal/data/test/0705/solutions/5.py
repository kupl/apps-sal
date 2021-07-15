n = int(input())
x = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
s = set(x+a)
count = 0
for i in x:
    for j in a:
        if i^j in s:
            count += 1
print('Karen' if count%2 == 0 else 'Koyomi')

