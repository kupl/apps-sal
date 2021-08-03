for _ in range(int(input())):
    a, b, c = map(int, input().split())
    answer = 0
    x = min(b, c // 2)
    answer += 3 * x
    b -= x
    x = min(a, b // 2)
    answer += 3 * x
    print(answer)
