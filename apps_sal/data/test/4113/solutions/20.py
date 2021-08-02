n = int(input())
#a, b = map(int,input().split())
#l = list(map(int,input().split()))
#l = [list(map(int,input().split())) for i in range(n)]

flag = 'No'

for i in range(0, n // 4 + 2):  # cake
    for j in range(0, n // 7 + 2):  # donuts
        if 4 * i + 7 * j == n:
            flag = 'Yes'
print(flag)
