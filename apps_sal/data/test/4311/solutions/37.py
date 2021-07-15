S = int(input())
s, c = S, 1
result = [s]
while True:
    if s % 2 == 0:
        s = s // 2
    elif s % 2 == 1:
        s = s * 3 + 1

    result.append(s)
    c += 1
    if len(set(result)) < len(result):
        break

print(c)
