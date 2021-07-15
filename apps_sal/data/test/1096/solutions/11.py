S = input()
x = ord(S[0]) - ord("a")
y = int(S[1]) - 1
ans = 8
is_x = False
is_y = False
if x == 0 or x == 7:
    is_x = True
if y == 0 or y == 7:
    is_y = True
if is_x and is_y:
    ans -= 5
elif (is_x and not is_y) or (not is_x and is_y):
    ans -= 3
print(ans)

