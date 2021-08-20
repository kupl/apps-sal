num = int(input())
colors = list(map(str, input().split()))
if colors.count('Y') > 0:
    print('Four')
else:
    print('Three')
