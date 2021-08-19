u = input()
length = list(input().split())
h = [int(i) for i in length]
if max(h) < sum(h) - max(h):
    print('Yes')
else:
    print('No')
