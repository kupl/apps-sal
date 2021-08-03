A, B, C = list(map(int, input().split()))
K = int(input())
Numbers = [A, B, C]

Numbers.sort(reverse=True)

for i in range(K):
    twice = Numbers[0] * 2
    Numbers[0] = twice

print((sum(Numbers)))
