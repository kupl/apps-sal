n = int(input())
st = list(input())
ans = 0
i = 0
while st and i < len(st):
    if st[i] == 'L':
        n -= i + 1
        st = st[i + 1:]
        i = -1
    elif st[i] == 'R':
        n -= 1
        j = i + 1
        while j < len(st):
            if st[j] == 'L':
                n -= j - i
                if (j - i) % 2 == 0:
                    n += 1
                st = st[j + 1:]
                i = -1
                break
            if st[j] == 'R':
                n -= j - i - 1
                st = st[j:]
                i = -1
                break
            j += 1
        else:
            n -= j - i - 1
    i += 1
print(n)
