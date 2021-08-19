N = int(input())
result = sum(list(map(int, str(N))))
if result % 9 == 0:
    print('Yes')
else:
    print('No')
