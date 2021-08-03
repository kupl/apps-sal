N, M = list(map(int, input().split()))

A = input().split()

count_one = A.count('1')

solution = []

queries = []
for i in range(M):
    Li, Ri = list(map(int, input().split()))
    if ((Ri - Li + 1) % 2 == 0 and
            (Ri - Li + 1) // 2 <= min(count_one, N - count_one)):
        solution.append('1')
        continue
    else:
        solution.append('0')

print('\n'.join(solution))
