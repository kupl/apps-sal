S = input() + '#'

pressed = []

prev = S[0]
count = 0
for s in S:
    if s == prev:
        count += 1
    else:
        prev = s
        pressed.append(count)
        count = 1

left_cumsum = []
right_cumsum = []

cumsum = 0
for count in pressed:
    cumsum += count
    left_cumsum.append(cumsum)

cumsum = 0
for count in pressed[::-1]:
    cumsum += count
    right_cumsum.append(cumsum)

length = len(left_cumsum)

if length == 1:
    print(len(S)-1)
    return

change_k = [0] * length

for idx in range(1, length):
    k = right_cumsum[-idx-1]
    change_k[idx-1] = k

for idx in range(1, length):
    k = left_cumsum[-idx-1]
    change_k[-idx] = max(change_k[-idx], k)

ans1 = min(change_k[::2])
ans2 = min(change_k[1::2])
print(max(ans1, ans2))
