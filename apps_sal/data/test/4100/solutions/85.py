n, k, q = list(map(int, input().split()))
arr = [k - q] * n

for _ in range(q):
    winner_id = int(input()) - 1
    arr[winner_id] += 1

for ele in arr:
    if ele > 0:
        print("Yes")
    else:
        print("No")
