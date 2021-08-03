N = str(input())

while True:
    N = N[0:-1]
    if len(N) % 2 == 0:
        if N[0:int(len(N) / 2)] == N[int(len(N) / 2):]:
            break

print(len(N))
