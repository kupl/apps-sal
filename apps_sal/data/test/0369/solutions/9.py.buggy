n, m = list(map(int, input().split()))
s = input()

one_sequence = 0
for i in range(1, n):
    if s[i] == "1":
        one_sequence += 1
        if one_sequence == m:
            print((-1))
            return
    else:
        one_sequence = 0

pos = n
ans = ""
while pos != 0:
    for i in range(1, m + 1)[::-1]:
        if pos - i < 0:
            continue
        if s[pos - i] != "1":
            ans = str(i) + " " + ans
            pos -= i
            break
print(ans)
