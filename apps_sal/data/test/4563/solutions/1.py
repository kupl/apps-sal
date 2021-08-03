n = int(input())
vote_t = 1
vote_a = 1

for _ in range(n):
    t, a = list(map(int, input().split()))
    n = max((vote_t + t - 1) // t, (vote_a + a - 1) // a)
    vote_t = n * t
    vote_a = n * a

print(vote_t + vote_a)
