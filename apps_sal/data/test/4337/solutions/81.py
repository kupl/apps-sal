N = int(input())
l = list(map(str, input().split()))
ln = len(set(l))
if ln == 3:
    print('Three')
else:
    print('Four')
