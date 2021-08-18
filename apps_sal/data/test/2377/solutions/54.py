n, h = list(map(int, input().split()))
bi_str = []
a_big = 0
ans = 0
a = [0] * n
b = [0] * n
for i in range(n):
    a[i], b[i] = list(map(int, input().split()))
    if a[i] > a_big:
        a_big = a[i]

for i in range(n):
    if b[i] > a_big:
        bi_str.append(b[i])
bi_str.sort(reverse=True)
if h <= sum(bi_str):
    for i in bi_str:
        if h > 0:
            h -= i
            ans += 1
        else:
            break
else:
    h -= sum(bi_str)
    ans += len(bi_str)
    ans += -(-h // a_big)
    '''
    if round(h/a_big) == h//a_big:
        ans += h//a_big
    else:
        ans += h//a_big+1
        '''

print(ans)
