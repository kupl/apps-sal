n = int(input())
a = input()
s = []
i = 1
st = 0
while i < n:
    if a[st] != a[i]:
        s.append(a[st])
        s.append(a[i])
        st = i + 1
        i = i + 2
    else:
        i += 1
print(n - len(s))
print(''.join(s))
