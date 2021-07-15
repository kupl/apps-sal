n = int(input())
s = input()
t = ""
cnt = 0
for si in s:
    t += si
    if len(t) >= 3 and t[-3:] == "fox":
        cnt += 1
        t = t[:-3]
print(n - cnt * 3)
