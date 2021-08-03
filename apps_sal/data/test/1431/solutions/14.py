n = int(input())
a = list(map(int, input().split()))

ball = [0 for i in range(n)]

for i in reversed(range(n)):
    if n // 2 < i:
        ball[i] = a[i]
    else:
        if (sum(ball[i::(i + 1)]) - a[i]) % 2 == 0:
            ball[i] = 0
        else:
            ball[i] = 1


num = [str(i + 1) for i, x in enumerate(ball) if x == 1]

if len(num) == 0:
    print('0')
else:
    print(len(num))
    num = ' '.join(num)
    print(num)
