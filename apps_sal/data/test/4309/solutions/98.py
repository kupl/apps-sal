N = int(input())
if N % 111 == 0:
    print(N)
else:
    for i in range(110):
        N += 1
        if N % 111 == 0:
            break
    print(N)
