n = int(input())
s = input().rstrip()
t = input().rstrip()

tobe_a = []
tobe_b = []
for i, (sch, tch) in enumerate(zip(s, t)):
    if sch == "b" and tch == "a":
        tobe_a.append(i + 1)
    elif sch == "a" and tch == "b":
        tobe_b.append(i + 1)

if (len(tobe_a) + len(tobe_b)) % 2 != 0:
    print(-1)
    return

ans = []
for a1, a2 in zip(tobe_a[::2], tobe_a[1::2]):
    ans.append((a1, a2))
for b1, b2 in zip(tobe_b[::2], tobe_b[1::2]):
    ans.append((b1, b2))

if len(tobe_a) % 2 == 1:
    ans.append((tobe_a[-1], tobe_a[-1]))
    ans.append((tobe_a[-1], tobe_b[-1]))

print(len(ans))
for a, b in ans:
    print(a, b)
