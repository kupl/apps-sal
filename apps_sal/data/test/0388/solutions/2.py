n, k = list(map(int, input().split()))
s = list(input().split())

def generate_name(n):
    s = ''
    for i in range(10):
        if (n == 0):
            break
        for j in range(26):
            n -= 1
            if (n == 0):
                s += chr(ord('A') + j)
                return s.title()
        s += 'Z'
    return s.title()

names = []
t = 1

for i in range(k - 1):
    names.append(generate_name(t))
    t += 1

for word in s:
    if word == 'YES':
        names.append(generate_name(t))
        t += 1
    else:
        names.append(names[-min(k - 1, len(names))])

print(' '.join(names))

