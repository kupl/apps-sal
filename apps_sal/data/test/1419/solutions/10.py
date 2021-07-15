
k = int(input())

initial = input()

B = [len(x) + 1 for sub in initial.split() for x in sub.split('-')]

B[-1] = B[-1] - 1


a, b, c = 0, len(initial), -1

while a < b:
    c = (a + b) // 2
    is_ok = True
    lines = 0
    current_line = c
    for word in B:
        if word > c:
            is_ok = False
        if current_line + word <= c:
            current_line += word
        else:
            lines += 1
            current_line = word

    if not is_ok or not lines <= k:
        a = c + 1
    else:
        b = c

print(a)

