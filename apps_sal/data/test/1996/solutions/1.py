n = int(input())

a = [chr(i) for i in range(97, 123)]
a = set(a)
cnt = 0
f = False
for i in range(n):
    r, w = input().split()
    w = set(list(w))
    if len(a) == 1:
        f = True
    if r == ".":
        a = a - w
    elif r == "!":
        a = a & w
        cnt += int(f)
    elif r == "?" and (i + 1) != n:
        a = a - w
        cnt += int(f)
print(cnt)
