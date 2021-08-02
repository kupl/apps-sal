n = int(input())
l = list(map(int, input().split()))
even = 0
for i in range(n):
    if l[i] % 2 == 0:
        even += 1
odd = n - even
if even > odd:
    print('READY FOR BATTLE')
else:
    print('NOT READY')
