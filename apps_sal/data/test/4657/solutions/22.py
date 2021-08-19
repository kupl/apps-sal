import sys
inf = sys.stdin
lines = inf.readlines()
q = int(lines[0])
for tests in range(q):
    (n, k) = (int(val) for val in lines[2 * tests + 1].split())
    candy = [int(val) for val in lines[2 * tests + 2].split()]
    odds = 0
    for i in candy:
        if i % 2 == 1:
            odds += 1
    if odds < k or sum(candy) % 2 != k % 2:
        print('NO')
    else:
        print('YES')
        count = 1
        for i in range(len(candy)):
            if count >= k:
                print(n)
                break
            if candy[i] % 2 == 1:
                print(i + 1, end=' ')
                count += 1
