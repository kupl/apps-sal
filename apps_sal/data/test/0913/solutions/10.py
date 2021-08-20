n = int(input())
r = input().split()
b = input().split()
if r.count('1') > b.count('1'):
    print(1)
else:
    x = b.count('1') - r.count('1') + 1
    count = 0
    for i in range(n):
        if r[i] == '1' and b[i] == '0':
            count += 1
    if count == 0:
        print(-1)
    elif x % count == 0:
        print(x // count + 1)
    else:
        print(x // count + 1 + 1)
