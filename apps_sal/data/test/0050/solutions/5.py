n, m, r = list(map(int, input().split()))
S = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]

stocks = r // min(S)
left = r % min(S)
newr = left + stocks * max(B)

print(max(r, newr))
