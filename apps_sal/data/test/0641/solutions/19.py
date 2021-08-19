s = input().split()
num = int(s[0])
if s[-1] == 'week':
    if num in (5, 6):
        print(53)
    else:
        print(52)
elif num < 30:
    print(12)
elif num == 30:
    print(11)
elif num == 31:
    print(7)
