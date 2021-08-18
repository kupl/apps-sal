def mp():
    return map(int, input().split())


n = int(input())
a = list(input())
if a == ['0']:
    print('0')
else:
    print('1' + '0' * a.count('0'))
