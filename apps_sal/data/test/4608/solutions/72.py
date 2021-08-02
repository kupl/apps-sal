n = int(input())
buttons = [int(input()) for _ in range(n)]
done = [0] * (n + 1)
next_button = buttons[0]
for _ in range(n):
    buttons_status = done[next_button]
    if buttons_status != 0:
        print((-1))
        return
    done[next_button] = 1
    if next_button == 2:
        break
    next_button = buttons[next_button - 1]
print((done.count(1)))
