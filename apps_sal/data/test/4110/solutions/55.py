from itertools import product

d, g = list(map(int, input().split()))
g //= 100
p, c = [], []
for _ in range(d):
    i, j = list(map(int, input().split()))
    p.append(i)
    c.append(j // 100)

# full search about complete bonuses
ans = sum(p)
for tf in product([True, False], repeat=d):
    score = 0
    cnt = 0

    for ind in range(d):
        if tf[ind]:
            cnt += p[ind]
            score += (ind + 1) * p[ind] + c[ind]
    
    for ind in range(d-1, -1, -1):
        if score >= g:
            break

        if tf[ind]:
            continue
        
        if (ind + 1) * p[ind] + score <= g:
            cnt += p[ind]
            score += (ind + 1) * p[ind]
        else:
            cnt += (g - score - 1) // (ind + 1) + 1
            score = g
    
    if score >= g and ans > cnt:
        ans = cnt

print(ans)

