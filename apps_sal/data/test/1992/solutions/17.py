(n, m, k) = map(int, input().split())
phone = list(map(int, input().split()))
action = list(map(int, input().split()))
positions = [0] * (n + 1)
for i in range(len(phone)):
    positions[phone[i]] = i
focus = 0
for i in action:
    focus += 1 + positions[i] // k
    if positions[i] > 0:
        (phone[positions[i]], phone[positions[i] - 1]) = (phone[positions[i] - 1], phone[positions[i]])
        positions[i] -= 1
        positions[phone[positions[i] + 1]] += 1
print(focus)
