N = int(input())
a = list(map(int, input().split()))
a.sort()
arrival = 1
ans = 0
while arrival < N:
    score = a.pop()
    if arrival == 1:
        ans += score
        arrival += 1
    else:
        ans += score * min(2, N - arrival)
        arrival += 2
print(ans)
