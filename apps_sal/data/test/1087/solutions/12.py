(n, k) = list(map(int, input().split()))
A = list(map(int, input().split()))
k_bin = '{:040b}'.format(k)
A_bin = list(['{:040b}'.format(x) for x in A])
X = ''
first = 1
for (i, col) in enumerate(zip(*A_bin)):
    if k_bin[i] == '0' and first:
        X += '0'
        continue
    if first:
        zero_cnt = col.count('0')
        one_cnt = n - zero_cnt
        if one_cnt < zero_cnt:
            X += '1'
        else:
            first = 0
            X += '0'
        continue
    zero_cnt = col.count('0')
    one_cnt = n - zero_cnt
    if one_cnt < zero_cnt:
        X += '1'
    else:
        X += '0'
X = int(X, 2)
ans = 0
for a in A:
    ans += X ^ a
print(ans)
