k = int(input())
q = input()
ans_strings = []
starts = []
for i in range(len(q)):
    if q[i] not in starts:
        if k > 1:
            starts.append(q[i])
            ans_strings.append(q[i])
            k -= 1
        elif k == 1:
            ans_strings.append(q[i::])
            k -= 1
            break
    else:
        ans_strings[len(ans_strings) - 1] += q[i]
if k == 0:
    print("YES")
    for i in ans_strings:
        print(i)
else:
    print("NO")
