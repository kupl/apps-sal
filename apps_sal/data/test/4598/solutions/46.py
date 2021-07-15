# キャンディーとN人の子供イージー

N = int(input())

answer = N + N * (N - 1) // 2

if 1 <= N <= 100:
    print(answer)
elif N <= 0 or 100 < N:
    print('Out of range')
