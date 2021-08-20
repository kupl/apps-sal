n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a1 = [a[i + 1] - a[i] for i in range(n - 1)]
b1 = [b[i + 1] - b[i] for i in range(n - 1)]
a1.sort()
b1.sort()
if a[0] != b[0] or a[-1] != b[-1]:
    print('No')
elif a1 == b1:
    print('Yes')
else:
    print('No')
