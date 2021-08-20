(s, p) = map(int, input().split())
for i in range(1, 1000001):
    if p % i != 0:
        continue
    elif i + p // i == s:
        print('Yes')
        break
else:
    print('No')
