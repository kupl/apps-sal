
s = input()
k = int(input())

c = s.count('1', 0, k)

x = s.replace('1', '')

if len(x) == 0:
    print(1)
else:
    if c == k:
        print(1)
    else:
        print(x[0])
