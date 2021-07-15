n, m, r = list(map(int,input().split()))
si = list(map(int,input().split()))
bi = list(map(int,input().split()))
print(max(r,r // min(si) * max(bi) + r % min(si)))

