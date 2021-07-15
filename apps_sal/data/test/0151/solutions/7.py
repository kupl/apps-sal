a = input()
gl = set(['a', 'e', 'i', 'o', 'u'])
cn = [0] * (200 + 1)
ans = []
for i in range(len(a)):
    if a[i] in gl:
        for i1 in range(ord('a'), ord('z') + 1):
            cn[i1] = 0
        continue
    cn[ord(a[i])] += 1
    st = set()
    cnt = 0
    for j in range(ord('a'), ord('z') + 1):
        if (chr(j) in gl) or cn[j] == 0:
            continue
        cnt += cn[j]
        st.add(j)
        if len(st) > 1 and cnt >= 3:
            ans.append(i)
            for i1 in range(ord('a'), ord('z') + 1):
                cn[i1] = 0
            cn[ord(a[i])] += 1
            break
for i in range(len(a)):
    if i in ans:
        print(' ', end='')
    print(a[i], end='')

