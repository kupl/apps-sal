# import sys
from collections import Counter
# input = sys.stdin.readline

# T = int(input())

# for t in range(T):
#     s = input()
#     pos = set(range(len(s)))

#     answer = ['']

#     for i in range(len(s)):
#         lets = [s[k] for k in pos]
#         if not pos:
#             break
#         cc = Counter(lets)
#         fl = cc.most_common()[0][0]
#         choice = ''
#         if fl == 'R':
#             choice = 'P'
#         elif fl == 'S':
#             choice = 'R'
#         else:
#             choice = 'S'
#         answer.append(choice)
#         next_pos = set()
#         for p in pos:
#             if s[p] == choice:
#                 np = p+1
#                 if np >= len(s):
#                     np = 0
#                 next_pos.add(np)
#         pos = next_pos

#     while len(answer) < len(s):
#         answer.append('R')

#     print(''.join(answer))

T = int(input())

for t in range(T):
    s = input()
    cc = Counter(s)
    fl = cc.most_common()[0][0]
    if fl == 'R':
        choice = 'P'
    elif fl == 'S':
        choice = 'R'
    else:
        choice = 'S'
    print(choice*len(s))

