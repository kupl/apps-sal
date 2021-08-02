m, n = list(map(int, input().split()))
l_n = list(map(int, input().split()))

l_n.sort(reverse=True)

total_vote = 0
pop_pd = []
ans = 'Yes'

for i in l_n:
    total_vote += i

for index, j in enumerate(l_n, 1):
    if index > n:
        break
    if total_vote / (4 * n) > j:
        ans = 'No'
        break

print(ans)
