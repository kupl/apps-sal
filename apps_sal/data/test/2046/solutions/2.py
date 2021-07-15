n = int(input())
used = [False] * (n + 1)
num = list(map(int, input().split()))
cur = n
for i in range(0, n):
    x = num[i]
    used[x] = True
    while(used[cur]):
        print(cur, end = ' ')
        cur -= 1
    print('')
    
