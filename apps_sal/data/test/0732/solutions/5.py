def cnt(s, p):

    ans = 0

    if p > s: ans = 0

    elif len(p) == len(s):

        ans = 1 if len(set(p.lstrip('0'))) <= 2 else 0

    elif len(set(p.lstrip('0'))) > 2: ans = 0

    elif s[:len(p)] > p:

        if len(set(p.lstrip('0'))) == 2:

            ans = 2**(len(s)-len(p))

        elif len(set(p.lstrip('0'))) == 1:

            ans = 1 + 9 * (2**(len(s)-len(p)) - 1)

        else:

            # ab for all a, b != 0

            ans = 10 + 45 * (2**(len(s)-len(p)) - 2)

            ans += 36 * sum([2**l-2 for l in range(2,len(s)-len(p))])

                

    else: ans = sum(cnt(s, p+c) for c in '0123456789')



    return ans



print(cnt(input().strip(), '')-1)





# Made By Mostafa_Khaled

