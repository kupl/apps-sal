s = input()
t = input()

length = len(s)

for _ in range(length):
    s = s[-1] + s[:length - 1]
    if s == t:
        print('Yes')
        break
else:
    print('No')
