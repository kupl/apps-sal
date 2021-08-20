n = int(input())
s = input()
diag = s[0]
notdiag = s[1]
result = 'YES'
if s[-1] != diag:
    result = 'NO'
if s[1:-1] != notdiag * len(s[1:-1]):
    result = 'NO'
if diag == notdiag:
    result = 'NO'
if result == 'YES':
    for i in range(1, n):
        s = input()
        if s[i] != diag or s[-i - 1] != diag:
            result = 'NO'
            break
        if i * 2 + 1 == n:
            line = s[:i] + s[i + 1:]
        else:
            i = min(i, n - i - 1)
            if i:
                line = s[:i] + s[i + 1:-i - 1] + s[-i:]
            else:
                line = s[:i] + s[i + 1:-i - 1]
        if line != notdiag * len(line):
            result = 'NO'
print(result)
