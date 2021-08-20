(n, k) = list(map(int, input().split()))
box_type = -1
ans_so_far = 99999999999999999999999
ans = 0
keys = [int(i) for i in input().split()]
for i in range(k):
    if n % keys[i] < ans_so_far:
        ans_so_far = n % keys[i]
        box_type = i + 1
        ans = n // keys[i]
print(box_type, ans)
