n = int(input())
t = input()
k = t.count('I')
if k > 1:
    print(0)
elif k == 1:
    print(1)
else:
    print(t.count('A'))
