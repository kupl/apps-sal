polygon_side = int(input())
side_length = list(map(int, input().split()))
if max(side_length) * 2 < sum(side_length):
    print('Yes')
else:
    print('No')
