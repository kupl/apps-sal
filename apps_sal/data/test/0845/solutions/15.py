keyboard = list("qwertyuiopasdfghjkl;zxcvbnm,./")
rorl = (-1, 1)[input() == "R"]
text = input()
ans = ""

for i in text:
    ans += keyboard[keyboard.index(i) - rorl]

print(ans)
