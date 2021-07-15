[m, n] = [int(x) for x in input().split()]

strings = []

for i in range(m):
    strings.append(input())

to_delete_index = [int(x)-1 for x in input().split()]
to_delete = [strings[int(x)] for x in to_delete_index]

base_len = len(to_delete[0])
for s in to_delete:
    if len(s) != base_len:
        print('No')
        return

match_string = ""
for i in range(base_len):
    match = to_delete[0][i]
    for s in to_delete:
        if s[i] != match:
            match = "?"
            break
    match_string += match

def match(s, match_string):
    if len(s) != len(match_string):
        return False

    for i in range(len(s)):
        if match_string[i] == "?":
            continue
        if match_string[i] != s[i]:
            return False
    return True

for i in range(len(strings)):
    if i in to_delete_index:
        continue
    if match(strings[i], match_string):
        print("No")
        return

print("Yes")
print(match_string)




