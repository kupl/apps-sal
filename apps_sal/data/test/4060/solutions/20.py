n = int(input())
S = input()

def solve(s, counts):
    openCount = 0
    closeCount = 0
    posCount = 0
    if n % 2 == 1:
        return posCount
    for i in range(n):
        if s[i] == '(':
            openCount += 1
        else:
            closeCount += 1
        if closeCount - openCount > 2:
            return posCount
        else:
            counts.append([openCount, closeCount])
    if abs(openCount-closeCount) == 2:
        if openCount > closeCount:
            s = s[::-1]
            s = ['(' if c == ')' else ')' for c in s]
            counts = []
            openCount = 0
            closeCount = 0
            for i in range(n):
                if s[i] == '(':
                    openCount += 1
                else:
                    closeCount += 1
                if closeCount - openCount > 2:
                    return posCount
                else:
                    counts.append([openCount, closeCount])
        for i in range(n):
            if counts[i][1] - counts[i][0] < 2 and s[i] == ')':
                posCount += 1
            if counts[i][1] > counts[i][0]:
                break
        return posCount
    else:
        return posCount

print(solve(S,[]))
