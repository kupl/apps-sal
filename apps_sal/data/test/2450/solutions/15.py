T = int(input())
for t in range(T):
    (N, M, x, y) = [int(_) for _ in input().split()]
    answer = 0
    for i in range(N):
        row = input().split('*')
        for el in row:
            if el:
                l = len(el)
                b2 = l // 2
                answer += min(2 * x * b2, y * b2)
                if l % 2:
                    answer += x
    print(answer)
