n = int(input())
alph = "abcdefghijklmnopqrstuvwxyz"
ch = ""
for x in range(n):
    ch += " " + input()


def f():
    ch1 = ""
    j = 0
    for k in range(26):
        for i in range(26):
            if ch1 + alph[i] not in ch:
                print(ch1 + alph[i])
                return
        ch1 = alph[j]
        j += 1


f()
