
s = list(input()) + ["R"]
n = len(s)

i = 1
r_start = 0
l_start = 0
l_last = 0
while i < n:
    if s[i - 1] == "R" and s[i] == "L":
        l_start = i
        i = i + 1
    elif s[i - 1] == "L" and s[i] == "R":
        l_last = i - 1
        for j in range(r_start, l_last + 1):
            if j == l_start - 1:
                if (l_last - r_start) % 2 == 1:
                    print((l_last - r_start) // 2 + 1, end=" ")
                else:
                    if (l_start - r_start) % 2 == 0:
                        print((l_last - r_start) // 2, end=" ")
                    else:
                        print((l_last - r_start) // 2 + 1, end=" ")
            elif j == l_start:
                if (l_last - r_start) % 2 == 1:
                    print((l_last - r_start) // 2 + 1, end=" ")
                else:
                    if (l_start - r_start) % 2 == 0:
                        print((l_last - r_start) // 2 + 1, end=" ")
                    else:
                        print((l_last - r_start) // 2, end=" ")
            else:
                print(0, end=" ")
        r_start = i
        i = i + 1
    else:
        i = i + 1
