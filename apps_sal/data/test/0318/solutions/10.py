__author__ = 'Utena'
time = list(map(int, input().split(':')))
n = int(input())
n = n + time[1]
time[0] = (n // 60 + time[0]) % 24
n = n % 60
time[1] = n
print(str(time[0]).zfill(2) + ':' + str(time[1]).zfill(2))
