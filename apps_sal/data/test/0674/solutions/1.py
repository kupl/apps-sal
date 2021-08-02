n = int(input())
A = []
for i in range(0, n):
    A = A + [input()]
start = [100] * 26
end = [100] * 26


def num(x):
    return(ord(x) - ord("a"))


def let(x):
    return(chr(x + ord("a")))


def ans(x):
    final = []
    for i in range(0, n):
        B = list(A[i])
        if len(B) == 1:
            if start[num(B[0])] == 100:
                start[num(B[0])] = -100
            if end[num(B[0])] == 100:
                end[num(B[0])] = -100
        else:
            for j in range(0, len(B)):
                if j == 0:
                    if start[num(B[j])] == 100 or start[num(B[j])] == -100:
                        start[num(B[j])] = -100
                    if end[num(B[j])] == 100 or end[num(B[j])] == -100:
                        end[num(B[j])] = num(B[j + 1])
                    elif end[num(B[j])] == num(B[j + 1]):
                        g = 0
                    else:
                        return("NO")
                elif 0 < j < len(B) - 1:
                    if start[num(B[j])] == 100 or start[num(B[j])] == -100:
                        start[num(B[j])] = num(B[j - 1])
                    elif start[num(B[j])] != num(B[j - 1]):
                        return("NO")
                    if end[num(B[j])] == 100 or end[num(B[j])] == -100:
                        end[num(B[j])] = num(B[j + 1])
                    elif end[num(B[j])] != num(B[j + 1]):
                        return("NO")
                elif j == len(B) - 1:
                    if end[num(B[j])] == 100:
                        end[num(B[j])] = -100
                    if start[num(B[j])] == 100 or start[num(B[j])] == -100:
                        start[num(B[j])] = num(B[j - 1])
                    elif start[num(B[j])] == num(B[j - 1]):
                        g = 0
                    else:
                        return("NO")
    if len(set(start)) + max(0, start.count(100) - 1) + max(0, start.count(-100) - 1) != 26:
        return("NO")
    elif len(set(end)) + max(0, end.count(100) - 1) + max(0, end.count(-100) - 1) != 26:
        return("NO")
    else:
        for i in range(0, 26):
            if start[i] != -100:
                g = 0
            else:
                final = final + [let(i)]
                j = end[i]
                while j != -100:
                    final = final + [let(j)]
                    j = end[j]
        if len(final) != len(set(start)) - min(1, start.count(100)) + max(0, start.count(-100) - 1):
            return("NO")
        else:
            return("".join(final))


print(ans(A))
