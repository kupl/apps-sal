n, k = list(map(int, input().split()))
st = input()
if (2 * k) <= n:
    for i in range(k - 1):
        print('LEFT')
    naprav = 'RIGHT'
else:
    for i in range(n - k):
        print('RIGHT')
    naprav = 'LEFT'
    st = st[::-1]
print('PRINT', st[0])
for i in range(1, len(st)):
    print(naprav)
    print('PRINT', st[i])
