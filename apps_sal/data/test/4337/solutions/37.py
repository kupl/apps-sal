N = int(input())
S = list(input().split())
quantity = len(list(set(S)))
if quantity == 3:
    print('Three')
else:
    print('Four')
