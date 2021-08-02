n, m, r = list(map(int, input().split()))
s = list(map(int, input().split()))
b = list(map(int, input().split()))
print(max((r // min(s)) * max(b) + (r % min(s)), r))
