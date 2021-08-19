t = int(input())
for iii in range(t):
    (n, k) = list(map(int, input().split()))
    i = 1
    while k > i:
        k -= i
        i += 1
    s = ['a'] * n
    s[-i - 1] = 'b'
    s[-k] = 'b'
    print(''.join(map(str, s)))
