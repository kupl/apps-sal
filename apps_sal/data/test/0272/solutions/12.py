correct = input()
incorrect = input()

other = dict()

for i in range(ord('a'), ord('z') + 1):
    other[chr(i)] = chr(i)

can = True

for i in range(len(correct)):
    if other[correct[i]] == incorrect[i]:
        continue

    if other[correct[i]] != correct[i]:
        can = False
        break

    if other[incorrect[i]] != incorrect[i]:
        can = False
        break

    other[correct[i]] = incorrect[i]
    other[incorrect[i]] = correct[i]

if can:
    for i in range(len(correct)):
        if other[correct[i]] != incorrect[i]:
            can = False
            break
if not can:
    print(-1)
else:
    ans = set()
    for i in range(ord('a'), ord('z') + 1):
        if other[chr(i)] != chr(i):
            a, b = i, ord(other[chr(i)])
            ans.add((chr(min(a, b)), chr(max(a, b))))

    print(len(ans))
    for x in ans:
        print(*x)
