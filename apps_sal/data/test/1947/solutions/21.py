(n, m, length_) = [int(s) for s in input().split(" ")]

a = [int(s) for s in input().split(" ")]

result = 0
prev = None
for i in range(n):
    if prev and prev <= (length_):
        if a[i] > length_:
            result += 1
    if not prev and a[i] > length_:
        result += 1

    prev = a[i]


for i in range(m):
    temp = input()
    if temp == "0":
        print(result)
    else:
        (_, p, d) = [int(s) for s in temp.split(" ")]
        num = p - 1
        cm = d
        old_val = a[num]
        a[num] += cm
        if old_val > length_:
            continue
        if a[num] <= length_:
            continue

        if num != 0 and num != (n - 1):
            if a[num - 1] > length_ and a[num + 1] > length_:
                result -= 1
            elif a[num - 1] <= length_ and a[num + 1] <= length_:
                result += 1
        elif num == 0 and (len(a) == 1 or a[1] <= length_):
            result += 1
        elif num == (n - 1) and a[n - 2] <= length_:
            result += 1
