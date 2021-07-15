t = int(input())
for q in range(t):
    answer = []
    n, k = map(int, input().split())
    q1 = 0
    while q1 < n:
        answer.append(chr(ord('a')+q1 % k))
        q1 += 1
    print(*answer, sep='')

