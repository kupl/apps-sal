N = int(input())
i = 1
if N == 1:
    print(i)
else:
    while i <= N:
        if((i * i) > N):
            print((i-1) * (i-1))
            break
        i += 1
