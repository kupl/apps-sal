(n, m) = list(map(int, input().split()))
reach = [0] * 100001
current = 1
count = [0] * 100001
a = list(map(int, input().split()))
ans = []
for i in a:
    count[i] += 1
    reach[count[i]] += 1
    if current == count[i] and reach[count[i]] == n:
        ans.append('1')
        current += 1
    else:
        ans.append('0')
print(''.join(ans))
