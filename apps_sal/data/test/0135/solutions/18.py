n, k = map(int, input().strip().split())

if k == 1:
    print('Yes')
else:
    '''
        prod = 1
    count = 2
    while prod < n:
        prod *= count
        if n % (prod - 1) == 0 and count >= k:
            rems = [n % i for i in range(1, k + 1)]
            if len(set(rems)) == len(rems):
                print('Yes')
                break
        count += 1
    else:
        print('No')
    '''
    if k > 50000:
        print('No')
    else:
        rems = [n % i for i in range(1, k + 1)]
        print('Yes' if len(set(rems)) == len(rems) else 'No')
