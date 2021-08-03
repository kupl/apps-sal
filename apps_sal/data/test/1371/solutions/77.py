S = int(input())
if S < 3:
    print(0)
else:
    count = [0] * (S + 1)
    count[0] = 1
    for i in range(3, S + 1):
        count[i] = count[i - 1] + count[i - 3]
    print((count[S]) % (10**9 + 7))
