N = int(input())
T = input()
if T == '1':
    print((2*(10**10)))
elif T == '11':
    print((10**10))
else:
    s = '110'
    for i in range(N//3+2):
        if T in s:
            print((10**10-i))
            return
        else:
            s += '110'
    print((0))

