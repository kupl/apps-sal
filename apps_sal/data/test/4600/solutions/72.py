(n, m) = map(int, input().split())
answer = 0
penalty = 0
ans = [0] * n
pen = [0] * n
for x in range(m):
    (p, s) = input().split()
    pi = int(p) - 1
    if ans[pi] == 1:
        continue
    if s == 'AC':
        answer += 1
        ans[pi] = 1
        penalty += pen[pi]
    elif s == 'WA':
        pen[pi] += 1
print(f'{answer} {penalty}')
