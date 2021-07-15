n = int(input())
s = input()
if "R" in s and "G" in s and "B" in s:
    print('BGR')
    return
if 'R' not in s and 'G' not in s:
    print('B')
    return
if 'R' not in s and 'B' not in s:
    print('G')
    return
if 'B' not in s and 'G' not in s:
    print('R')
    return

if "R" in s and "G" in s:
    answer = 'B'
    if s.count('R') > 1:
        answer += 'G'
    if s.count('G') > 1:
        answer += 'R'
    print(answer)
    return
if "R" in s and "B" in s:
    answer = 'G'
    if s.count('R') > 1:
        answer = 'B' + answer
    if s.count('B') > 1:
        answer += 'R'
    print(answer)
    return
if "B" in s and "G" in s:
    answer = 'R'
    if s.count('B') > 1:
        answer = 'G' + answer
    if s.count('G') > 1:
        answer = 'B' + answer
    print(answer)
    return
