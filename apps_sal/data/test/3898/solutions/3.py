n = int(input())
start = [x for x in input().split(' ') if not x == '0']
end = [x for x in input().split(' ') if not x == '0']

index1 = start.index('1')
index2 = end.index('1')

for i in range(n - 1):
    if not start[index1] == end[index2]:
        print('NO')
        break
    index1 = (index1 + 1) % (n - 1)
    index2 = (index2 + 1) % (n - 1)
else:
    print('YES')
