n = int(input())
a = list(map(int, input().split()))
ans = True
for i in a:
    if i % 2 == 0:
        if i % 3 != 0 and i % 5 != 0:
            ans = False
print('APPROVED' if ans else 'DENIED')
