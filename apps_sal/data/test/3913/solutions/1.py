from string import ascii_lowercase as lower
char = int(input())
s = input()
new = [input() for k in range(int(input()))]
used = set()
can_be_said = set(lower)
indices = []
others = []
for index in range(char):
    if s[index] != '*':
        used.add(s[index])
        others.append(index)
    else:
        indices.append(index)
for word in new:
    now = set()
    for i in indices:
        now.add(word[i])
    is_ = True
    for i in others:
        if s[i] != word[i]:
            is_ = False
    if not is_:
        continue
    if len(now.intersection(used)) == 0:
        can_be_said = can_be_said.intersection(now)
can_be_said = can_be_said - used
print(len(can_be_said))
