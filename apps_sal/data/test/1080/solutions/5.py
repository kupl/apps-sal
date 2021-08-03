n = int(input())
a = list(map(int, input().split()))
#print(sum(a), max(a))
if(sum(a) < 2 * max(a) or sum(a) % 2 == 1):
    print('NO')
else:
    print('YES')
