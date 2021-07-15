N = int(input())
if N % 2 == 0:
    answer = 0
    N //= 2
    for i in range(100):
        answer += N // 5
        N //= 5
    print(answer)
else:
    print('0')
