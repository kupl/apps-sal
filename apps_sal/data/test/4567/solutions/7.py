N = int(input())
S = sorted([int(input()) for _ in range(N)])
t = sum(S)
if t % 10 != 0:
    print(sum(S))
else:
    for i in S:
        if (t - i) % 10 != 0:
            print(t - i)
            break
    else:
        print(0)
