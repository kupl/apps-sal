K = int(input())
A, B = map(int, input().split())
ans = 0

for i in range(1000):
    if A <= K * i and K * i <= B:
        ans += 1

if ans == 0:
    print('NG')
else:
    print('OK')
