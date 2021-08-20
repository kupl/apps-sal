n = int(input())
a = list(map(int, input().split()))
first = False
for i in a:
    if i % 2 == 1:
        first = True
        break
if first:
    print('First')
else:
    print('Second')
