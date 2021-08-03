from _collections import deque

for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    ar = list(map(int, input().split()))
    picks = 0
    lol = deque([])
    for i in range(1, k - 1):
        if ar[i - 1] < ar[i] > ar[i + 1]:
            picks += 1
            lol.append(i)
    max_picks = picks
    ans = 0
    for i in range(k - 1, n - 1):
        if len(lol) > 0 and lol[0] == i - k + 2:
            lol.popleft()
            picks -= 1
        if ar[i - 1] < ar[i] > ar[i + 1]:
            picks += 1
            lol.append(i)
        if picks > max_picks:
            max_picks = picks
            ans = i - k + 2
    print(max_picks + 1, ans + 1)
