n, m = [int(i) for i  in input().split()]
if n == 1:
    print(1)
else:
    if n-m>m-1:
        print(m+1)
    else:
        print(m-1)

