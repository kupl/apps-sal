import sys
spies, turns, note, final = list(map(int, input().split()))
if note < final:
    next = 1
else:
    next = -1
answer = []


def pass_note(current_turn, next_watch, left, right, note):
    #    print(f'\n{current_turn}), next watch: {next_watch}, left: {left}, right: {right} has note: {note}, goal: {final}')
    if current_turn == next_watch:
        #        print('Watched this turn')
        if note in range(left, right + 1) or note + next in range(left, right + 1):
            #            if note in range(left, right + 1):
            #                print(f'Im being watched')
            #            else:
            #                print(f'Guy to pass it to is being watched')
            return note, 'X'
#    print('Not watched, passing note to ', end='')
    if note < final:
        note += next
#        print('right')
        return note, 'R'
    else:
        note += next
#        print('left')
        return note, 'L'


current_turn = 0
for turn in range(turns):
    next_watch, left, right = list(map(int, input().split()))
    while current_turn < next_watch:
        current_turn += 1
        note, ans = pass_note(current_turn, next_watch, left, right, note)
        answer.append(ans)
        if note == final:
            print(''.join(answer))
            return

#print("ran out of turns")

while note != final:
    #    print(f'Note at: {note}, goal is {final}')
    current_turn += 1
    note, ans = pass_note(current_turn, 0, -1, -1, note)
    answer.append(ans)

print(''.join(answer))
