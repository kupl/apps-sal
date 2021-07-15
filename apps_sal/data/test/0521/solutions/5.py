n = int(input())
canvas = input()

unknown_status = False
if canvas[0] == '?' or canvas[-1] == '?':
    unknown_status = True
for i in range(1, n-1):
    if canvas[i] == '?':
        if canvas[i+1] == '?':
            unknown_status = True
            break
        elif canvas[i-1] == canvas[i+1]:
            unknown_status = True
            break

adjust_status = True
for i in range(n-1):
    if canvas[i] == canvas[i+1] and canvas[i] != '?':
        adjust_status = False
        break

print("Yes" if unknown_status and adjust_status else "No")

