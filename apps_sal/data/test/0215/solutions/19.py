size = int(input())
n = input()
rez = []
ans = 0
yet = 0
for i in n:
    if ord(i) > 96 and i not in rez:
        rez.append(i)
        yet += 1
    elif ord(i) < 96:
        rez = []
        yet = 0
    ans = max(ans, yet)
print(ans)
