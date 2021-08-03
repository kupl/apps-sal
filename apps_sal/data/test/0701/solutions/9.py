s = input()
t = input()
array = automaton = both = 1

# array swapaet
let = set(s) | set(t)
if len(s) == len(t):
    for i in let:
        if s.count(i) != t.count(i):
            array = 0
else:
    array = 0

if array:
    print('array')
    return

# automaton dalyaet
f = s
i = 0

while i < min(len(t), len(f)):
    if f[i] != t[i]:
        f = f[:i] + f[i + 1:]
    else:
        i += 1

if f[:len(t)] == t:
    print('automaton')
    return

# both
for i in let:
    if s.count(i) < t.count(i):
        both = 0
if both:
    print('both')
    return

# else
print('need tree')
