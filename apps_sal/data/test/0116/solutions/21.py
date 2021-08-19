(l1, r1, l2, r2, k) = map(int, input().split())
answer = min(r1, r2) - max(l1, l2) + 1
if min(r1, r2) >= k >= max(l1, l2):
    answer -= 1
print(max(0, answer))
