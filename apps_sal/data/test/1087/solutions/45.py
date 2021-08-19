(n, k) = map(int, input().split())
A = list(map(int, input().split()))
k_bin = '{:040b}'.format(k)
A_bin = list(map(lambda x: '{:040b}'.format(x), A))
X = ''
limited = 1
for (i, col) in enumerate(zip(*A_bin)):
    if k_bin[i] == '0' and limited:
        X += '0'
        continue
    zero_cnt = col.count('0')
    one_cnt = n - zero_cnt
    if one_cnt < zero_cnt:
        X += '1'
    else:
        X += '0'
        limited = 0
X = int(X, 2)
print(sum((X ^ a for a in A)))
