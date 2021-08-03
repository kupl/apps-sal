K = int(input())
A, B = map(int, input().split())
cnt = 0

for i in range(B // K + 1):
    if A <= K * i and K * i <= B:
        cnt += 1
print('OK' if cnt > 0 else 'NG')
