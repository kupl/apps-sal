s = input()
t = input()
val = 1000
for i in range(len(s) - len(t) + 1):
    cnt = 0
    for j in range(len(t)):
        if s[i + j] != t[j]:
            cnt += 1
    val = min(val, cnt)
print(val)
