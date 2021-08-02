def check():
    nonlocal arr1, arr2, s1, s2
    for i in range(26):
        if arr1[i] != arr2[i]:
            print(-1)
            return

    start = 0
    out = []
    while start < len(s1):
        if s1[start] == s2[start]:
            start += 1
            continue

        if s2[start] != s1[start]:
            req_index = -1
            for i in range(start + 1, len(s2)):
                if s1[i] == s2[start]:
                    req_index = i
                    break
            for i in range(req_index, start, -1):
                s1[i], s1[i - 1] = s1[i - 1], s1[i]
                out.append(i)
        start += 1

    if s1 == s2:
        if len(out) <= 10000:
            print(len(out))
            for o in out:
                print(o, end=" ")
            print()
        else:
            print(-1)
    else:
        print(-1)


n = int(input())

s1 = list(input())
s2 = list(input())

arr1 = [0] * 26
arr2 = [0] * 26

for i in range(len(s1)):
    arr1[ord(s1[i]) - 97] += 1
    arr2[ord(s2[i]) - 97] += 1


check()
