l = int(input())
v_count = 1
additional_e = []
while True:
    if l == 1:
        break
    elif l % 2 == 0:
        l = l // 2
        v_count += 1
    elif l % 2 == 1:
        l -= 1
        additional_e.append(v_count)
print((v_count, (v_count - 1) * 2 + len(additional_e)))
for i in range(1, v_count):
    print((i, i + 1, 0))
    print((i, i + 1, 2 ** (i - 1)))
num = 2 ** (v_count - 1)
for i in additional_e[::-1]:
    print((i, v_count, num))
    num = num + 2 ** (i - 1)
