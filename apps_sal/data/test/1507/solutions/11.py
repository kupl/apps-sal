string_len, condition_value = (int(x) for x in input().split())
idx___letter = list(input())

letter___start__finish = {}

for idx, letter in enumerate(idx___letter):
    if letter not in letter___start__finish:
        letter___start__finish[letter] = [idx, idx]
    if letter___start__finish[letter][1] < idx:
        letter___start__finish[letter][1] = idx

max_events_open = 0
curr_events_open = 0
for idx, letter in enumerate(idx___letter):
    start, close = letter___start__finish[letter]
    if idx == start:
        curr_events_open += 1
        max_events_open = max(max_events_open, curr_events_open)
    if idx == close:
        curr_events_open -= 1
if max_events_open > condition_value:
    print('YES')
else:
    print('NO')


