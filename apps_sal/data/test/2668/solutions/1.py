# cook your dish here
j, s, m = list(map(int, input().split()))
m -= j
if (m // s) % 2 == 0:
    print('Lucky Chef')

else:
    print('Unlucky Chef')
