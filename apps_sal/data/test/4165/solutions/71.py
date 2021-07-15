N = int(input())
L = list(map(int, input().split()))
long = max(L)
other = sum(L) - long

if long < other:
    print('Yes')
else:
    print('No')
