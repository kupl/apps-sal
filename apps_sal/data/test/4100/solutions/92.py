(N, K, Q) = map(int, input().split())
answers = [K - Q] * N
for _ in range(Q):
    a = int(input())
    answers[a - 1] += 1
for ans in answers:
    if ans > 0:
        print('Yes')
    else:
        print('No')
