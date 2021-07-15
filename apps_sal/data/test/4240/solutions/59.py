S = input()
T = str(input())

s = list(S)
s_len = len(S)

i = 0

while i < s_len:
    s.insert(0, s[-1])
    s.pop(-1)
    new_s = "".join(s)
    i += 1
    if new_s == T:
        print("Yes")
        break
else:
    print("No")
