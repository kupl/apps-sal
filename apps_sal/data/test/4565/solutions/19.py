N = int(input())
S = input()
e = S.count("E")
cnt = e
for i in S:
    if i == "E":
        cnt -= 1
    else:
        cnt += 1
    e = min(e, cnt)
print(e)
