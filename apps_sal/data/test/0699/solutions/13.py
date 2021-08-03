data = input().split()

Y, K, N = int(data[0]), int(data[1]), int(data[2])

answer = []
i = K
while i <= N:
    if i > Y:
        answer.append(i - Y)
    i += K

if len(answer) == 0:
    print('-1')
else:
    print(" ".join(map(str, answer)))
