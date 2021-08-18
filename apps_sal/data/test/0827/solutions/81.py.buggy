# TODO refactor

n = int(input())
t = input()

if t == '1':
    print((2 * 10**10))
else:
    if '0' in t:
        first_zero = t.index('0')
    else:
        first_zero = n
    if first_zero < 3 and all(c == '1' for c in t[:first_zero]):
        num_of_110 = 0
        curr = t[first_zero + 1:]
        while len(curr) > 3 and curr.startswith('110'):
            num_of_110 += 1
            curr = curr[3:]
        if curr in ['1', '11', '110']:
            num_of_110 += 1
        elif not curr:
            pass
        else:
            print((0))
            import sys
            return
        print((10**10 - num_of_110))
    else:
        print((0))
