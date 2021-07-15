n = int(input())

zeros = 0
ugly = '1'
for s in input().split():
    if s == '0':
        print('0')
        import sys; return
    beautiful = True
    ones = 0
    for ch in s:
        if ord(ch) > 49:
            beautiful = False
            break
        if ord(ch) == 49:
            if ones == 1:
                beautiful = False
                break
            ones = 1
    if beautiful:
        zeros += len(s) - 1
    else:
        ugly = s

print(ugly + zeros * '0')

