n, k = map(int, input().strip().split())

if k == 1:
    print('Yes')
else:
    # k! - 1 must divide into n
    '''
        prod = 1
    count = 2
    while prod < n:
        prod *= count
        if n % (prod - 1) == 0 and count >= k:
            #res = n // (prod - 1)
            # note: existance means k must be really small
            rems = [n % i for i in range(1, k + 1)]
            #print(rems)
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
        # print(rems)
        print('Yes' if len(set(rems)) == len(rems) else 'No')
