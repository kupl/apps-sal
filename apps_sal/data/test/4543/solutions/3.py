a, b = (i for i in input().split())
c = int(a + b)
ans = c ** 0.5
if float.is_integer(ans):
    print('Yes')
else:
    print('No')
