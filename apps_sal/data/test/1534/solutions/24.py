# python3
# utf-8

string = input()
prefix___a_nr = [0]
prefix___b_nr = [0]
for sym in string:
    curr_a_nr = prefix___a_nr[-1]
    curr_b_nr = prefix___b_nr[-1]
    if sym == 'a':
        curr_a_nr += 1
    elif sym == 'b':
        curr_b_nr += 1
    prefix___a_nr.append(curr_a_nr)
    prefix___b_nr.append(curr_b_nr)

ans = 5000
for sep1 in range(len(string) + 1):
    for sep2 in range(sep1, len(string) + 1):
        curr_ans = 0
        curr_ans += prefix___b_nr[sep1]
        curr_ans += prefix___a_nr[sep2] - prefix___a_nr[sep1]
        curr_ans += prefix___b_nr[-1] - prefix___b_nr[sep2]
        ans = min(ans, curr_ans)
print(len(string) - ans)
