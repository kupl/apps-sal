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
    elif not s or s[-1] < a[j]:
        ans.append('R')
        s.append(a[j])
        j -= 1
    elif not s or s[-1] < a[i]:
        s.append(a[i])
        ans.append('L')
        i += 1
    else:
        break
print(len(s))
print(''.join(ans))
