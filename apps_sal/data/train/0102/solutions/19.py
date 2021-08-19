n = int(input())
for i in range(n):
    t = int(input())
    answer = 0
    for i in range(1, 10):
        k = i
        while k <= t:
            answer += 1
            k = k * 10 + i
    print(answer)
