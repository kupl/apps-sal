(n, k) = map(int, input().strip().split())
if k == 1:
    print('Yes')
else:
    "\n        prod = 1\n    count = 2\n    while prod < n:\n        prod *= count\n        if n % (prod - 1) == 0 and count >= k:\n            #res = n // (prod - 1)\n            # note: existance means k must be really small\n            rems = [n % i for i in range(1, k + 1)]\n            #print(rems)\n            if len(set(rems)) == len(rems):\n                print('Yes')\n                break\n        count += 1\n    else:\n        print('No')\n    "
    if k > 50000:
        print('No')
    else:
        rems = [n % i for i in range(1, k + 1)]
        print('Yes' if len(set(rems)) == len(rems) else 'No')
