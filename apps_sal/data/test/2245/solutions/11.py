from sys import stdin
c = int(stdin.readline().strip())
for i in range(c):
    (n, m) = list(map(int, stdin.readline().strip().split()))
    if n == 0:
        print('Bob')
        continue
    if m % 3 == 0:
        n = n % (m + 1)
        if (n == 0 or n % 3 == 0) and n != m:
            print('Bob')
        else:
            print('Alice')
        continue
    if n % 3 == 0:
        print('Bob')
    else:
        print('Alice')
'\nk=6\ndp=["B","A","A"]\nfor i in range(3,30):\n    n=len(dp)\n    if n-k>=0:\n        if dp[n-1]=="B" or dp[n-2]=="B" or dp[n-k]=="B":\n            dp.append("A")\n            continue\n        else:\n            dp.append("B")\n            continue\n    else:\n        if dp[n-1]=="B" or dp[n-2]=="B":\n            dp.append("A")\n            continue\n        else:\n            dp.append("B")\n            continue  \n        \n'
