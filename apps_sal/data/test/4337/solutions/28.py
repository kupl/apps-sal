n = int(input())
s = list(map(str, input().split()))
if s.count('Y') == 0:
    print('Three')
else:
    print('Four')
