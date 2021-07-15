N = int(input())
place = N
word = True
numbers = list(map(int, input().split()))
for i in range(1, N):
    if numbers[i] < numbers[i - 1]:
        place = i
        for i in range(place + 1, place + N):
            if numbers[i % N] < numbers[i % N - 1]:
                word = False
                break
        break
if word == False:
    print(-1)
else:
    print(N - place)
