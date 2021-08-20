N = int(input())
a = input()
b = int(N // 2)
if N % 2 != 0 or a[0:b] != a[b:N]:
    print('No')
else:
    print('Yes')
