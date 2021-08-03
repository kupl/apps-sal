s = input()
prev = ""
cnt = 0
for elem in s:
    if elem == "v" and prev == "v":
        cnt += 1
    prev = elem
n = 0
prev = ""
ans = 0
for elem in s:
    if elem == "v" and prev == "v":
        n += 1
    if elem == "o":
        ans += n * (cnt - n)
    prev = elem
print(ans)
