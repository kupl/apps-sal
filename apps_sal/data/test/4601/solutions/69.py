a = list(map(int, input().split()))
b = list(map(int, input().split()))
if len(b) <= a[1]:
    print('0')
elif a[1] == 0:
    print(sum(b))
else:
    b.sort(reverse=True)
    print(sum(b[a[1]:]))
