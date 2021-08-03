n = int(input())
a = [int(item) for item in input().split()]

s = []
i = 0
j = n - 1
ans = []
while i <= j:
    if a[i] < a[j]:
        if not s or s[-1] < a[i]:
            s.append(a[i])
            ans.append('L')
            i += 1
        elif not s or s[-1] < a[j]:
            s.append(a[j])
            ans.append('R')
            j -= 1
        else:
            break
    elif a[i] > a[j]:
        if not s or s[-1] < a[j]:
            ans.append('R')
            s.append(a[j])
            j -= 1
        elif not s or s[-1] < a[i]:
            s.append(a[i])
            ans.append('L')
            i += 1
        else:
            break
    else:
        p1 = 0
        p2 = 0
        cur_last = s[-1] if s else None
        or_i = i
        while i <= j and (cur_last is None or a[i] > cur_last):
            cur_last = a[i]
            i += 1
            p1 += 1

        cur_last = s[-1] if s else None
        while or_i <= j and (cur_last is None or a[j] > cur_last):
            cur_last = a[j]
            j -= 1
            p2 += 1
        if p1 > p2:
            ans += list("L" * p1)
        else:
            ans += list("R" * p2)
        break

print(len(ans))
print(''.join(str(x) for x in ans))
