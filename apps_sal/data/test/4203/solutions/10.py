S = input()

if S[0] != "A":
    print("WA")
    return

if "C" not in S[2:-1]:
    print("WA")
    return

c_cnt = 0
for i in range(1, len(S)):
    if S[i] == "C":
        c_cnt += 1
    elif S[i].isupper():
        print("WA")
        return
    if c_cnt >= 2:
        print("WA")
        return

print("AC")
