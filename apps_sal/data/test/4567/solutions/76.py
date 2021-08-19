N = int(input())
s = [int(input()) for _ in range(N)]
xs = [x % 10 for x in s]
if xs.count(0) == N:
    print(0)
elif sum(s) % 10 != 0:
    print(sum(s))
else:
    minimum = 999
    for n in range(N):
        if s[n] % 10 != 0:
            minimum = min(minimum, s[n])
    print(sum(s) - minimum)
