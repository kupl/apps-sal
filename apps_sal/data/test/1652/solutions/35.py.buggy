# dream dreamer erase eraser
import sys

S = input()
index = len(S)
while index > 7:
    five = S[index - 5:index]
    six = S[index - 6:index]
    seven = S[index - 7:index]
    if five == "dream" or five == "erase":
        index -= 5
    elif six == "eraser":
        index -= 6
    elif seven == "dreamer":
        index -= 7
    else:
        print("NO")
        return

last = S[:index]
if last == "dream" or last == "erase" or last == "eraser" or last == "dreamer":
    print("YES")
else:
    print("NO")
