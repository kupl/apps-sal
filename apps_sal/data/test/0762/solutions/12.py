(n, k) = list(map(int, input().split()))
seq = list(map(int, input().split()))
curr = 0
cut = []
for i in range(n - 1):
    if seq[i] % 2:
        curr += 1
    else:
        curr -= 1
    if curr == 0:
        cut.append(abs(seq[i] - seq[i + 1]))
cut.sort()
ans = 0
currsum = 0
for i in cut:
    currsum += i
    if currsum > k:
        break
    else:
        ans += 1
print(ans)
